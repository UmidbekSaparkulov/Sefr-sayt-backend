import json
from django.core.management.base import BaseCommand
from listening.models import ListeningTest, ListeningQuestion, ListeningOption
from core.models import Level, Skill

class Command(BaseCommand):
    help = "Load listening test data from JSON file (Skill and Level by name)"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to JSON file")
        parser.add_argument("--skill", type=str, required=True, help="Skill name (e.g., Listening)")
        parser.add_argument("--level", type=str, required=True, help="Level name (e.g., B1)")

    def handle(self, *args, **options):
        file_path = options["file_path"]
        skill_name = options["skill"]
        level_name = options["level"]

        # Skill va Level mavjud bo'lmasa, yaratadi
        skill, _ = Skill.objects.get_or_create(name=skill_name)
        level, _ = Level.objects.get_or_create(name=level_name)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stderr.write(f"File not found: {file_path}")
            return

        for test_data in data:
            listening_test = ListeningTest.objects.create(
                skill=skill,
                level=level,
                title=test_data["title"],
                type=test_data["type"],
                audio_file=test_data["audio_file"]
            )

            self.stdout.write(f"Created ListeningTest: {listening_test.title}")

            for order, q_data in enumerate(test_data["questions"], 1):
                question = ListeningQuestion.objects.create(
                    listening_test=listening_test,
                    order=order,
                    text=q_data["text"],
                    correct_answer=q_data["correct"]
                )

                for key, text in q_data["options"].items():
                    ListeningOption.objects.create(
                        question=question,
                        key=key,
                        text=text,
                        is_correct=(key == q_data["correct"])
                    )

                self.stdout.write(f"  Added question {order}")

        self.stdout.write(self.style.SUCCESS("Successfully loaded all listening tests!"))
