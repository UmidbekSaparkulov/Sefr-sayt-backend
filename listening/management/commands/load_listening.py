# listening/management/commands/load_listening.py
import csv
from django.core.management.base import BaseCommand
from core.models import Level, Skill
from listening.models import ListeningTest, ListeningQuestion, ListeningOption

class Command(BaseCommand):
    help = "Load Listening data from CSV file into the database"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # 1️⃣ Level va Skill obyektlari
                level, _ = Level.objects.get_or_create(name=row['level'])
                skill, _ = Skill.objects.get_or_create(name=row['skill'])

                # 2️⃣ ListeningTest obyektini yaratish yoki topish
                test, _ = ListeningTest.objects.get_or_create(
                    title=row['title'],
                    level=level,
                    skill=skill,
                    defaults={
                        'type': row.get('type', ''),
                        'audio_file': row.get('audio_file', ''),
                        'transcript': row.get('transcript', ''),
                        'instructions': row.get('instructions', ''),
                        'language': row.get('language', 'en'),
                    }
                )

                # 3️⃣ ListeningQuestion obyektini yaratish yoki topish
                question, _ = ListeningQuestion.objects.get_or_create(
                    listening_test=test,
                    order=int(row.get('order') or 1),
                    defaults={
                        'text': row.get('question_text', ''),
                        'question_type': row.get('question_type', 'multiple-choice'),
                        'correct_answer': row.get('correct_answer', ''),
                    }
                )

                # 4️⃣ ListeningOption obyektini yaratish
                if row.get('option_key') and row.get('option_text'):
                    is_correct_str = row.get('is_correct', '').strip().lower()
                    is_correct = is_correct_str in ('true', '1', 'yes')
                    ListeningOption.objects.get_or_create(
                        question=question,
                        key=row['option_key'],
                        defaults={
                            'text': row['option_text'],
                            'is_correct': is_correct,
                        }
                    )

            self.stdout.write(self.style.SUCCESS("✅ Listening data successfully loaded!"))
