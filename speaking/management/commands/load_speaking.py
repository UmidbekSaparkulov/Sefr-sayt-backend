import csv
from django.core.management.base import BaseCommand
from speaking.models import Speaking


class Command(BaseCommand):
    help = "CSV fayldan Speaking ma'lumotlarini yuklash"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="CSV fayl manzili")

    def handle(self, *args, **options):
        csv_file = options["csv_file"]

        with open(csv_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)

            count = 0
            for row in reader:
                part = row.get("part")
                topic = row.get("topic")
                question = row.get("question")
                audio_file = row.get("audio_file")  # optional

                Speaking.objects.get_or_create(
                    part=part,
                    topic=topic,
                    question=question,
                    defaults={"audio_file": audio_file},
                )
                count += 1

            self.stdout.write(self.style.SUCCESS(f"{count} ta Speaking yozuv yuklandi ✅"))
