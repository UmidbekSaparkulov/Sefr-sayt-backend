import json
from django.core.management.base import BaseCommand
from core.models import Level, Skill
from reading.models import ReadingTest, Option, Question, Segment, Paragraph, Heading

class Command(BaseCommand):
    help = "Load Reading test data from JSON into the database"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)

        for test_data in data:
            # 1️⃣ Level va Skill obyektlarini olish yoki yaratish
            level_name = test_data.get('level', 'Unknown')
            skill_name = test_data.get('skill', 'Reading')

            level, _ = Level.objects.get_or_create(name=level_name)
            skill, _ = Skill.objects.get_or_create(name=skill_name)

            # 2️⃣ ReadingTest yaratish yoki topish
            test, _ = ReadingTest.objects.get_or_create(
                title=test_data.get('title', 'Untitled'),
                level=level,
                skill=skill,
                defaults={
                    'type': test_data.get('type', ''),
                    'language': test_data.get('language', 'en'),
                    'instructions': test_data.get('instructions', ''),
                    'passage': test_data.get('passage', ''),
                }
            )

            # 3️⃣ Options
            for option in test_data.get('options', []):
                Option.objects.get_or_create(
                    reading_test=test,
                    key=option.get('key', ''),
                    defaults={
                        'word': option.get('word', ''),
                        'text': option.get('text', ''),
                    }
                )

            # 4️⃣ Questions
            for q_index, question in enumerate(test_data.get('questions', []), start=1):
                Question.objects.get_or_create(
                    reading_test=test,
                    order=q_index,
                    text=question.get('text', ''),
                    defaults={
                        'question_type': question.get('type', 'multiple-choice'),
                        'correct_answer': question.get('answer', ''),
                    }
                )

            # 5️⃣ Segments
            for s_index, segment in enumerate(test_data.get('segments', []), start=1):
                # Segmentlar arrayda dict ko‘rinishida bo‘lishi kerak
                if isinstance(segment, dict) and 'gap' in segment:
                    Segment.objects.get_or_create(
                        reading_test=test,
                        order=s_index,
                        defaults={
                            'gap_number': segment.get('gap'),
                            'text_before': '',
                            'text_after': '',
                        }
                    )
                elif isinstance(segment, str):
                    Segment.objects.get_or_create(
                        reading_test=test,
                        order=s_index,
                        defaults={
                            'text_before': segment,
                        }
                    )

            # 6️⃣ Paragraphs
            for p_index, para in enumerate(test_data.get('paragraphs', []), start=1):
                Paragraph.objects.get_or_create(
                    reading_test=test,
                    order=p_index,
                    defaults={
                        'text': para.get('text', ''),
                    }
                )

            # 7️⃣ Headings
            for heading in test_data.get('headings', []):
                Heading.objects.get_or_create(
                    reading_test=test,
                    key=heading.get('key', ''),
                    defaults={
                        'text': heading.get('text', ''),
                    }
                )

        self.stdout.write(self.style.SUCCESS('✅ All Reading data successfully loaded!'))
