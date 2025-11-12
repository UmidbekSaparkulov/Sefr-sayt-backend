import csv
from django.core.management.base import BaseCommand
from writing.models import Writing


class Command(BaseCommand):
    help = "CSV fayldan Writing ma'lumotlarini yuklash"

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

                Writing.objects.get_or_create(
                    part=part,
                    topic=topic,
                    question=question
                )
                count += 1

            self.stdout.write(self.style.SUCCESS(f"{count} ta Writing yozuv yuklandi ✅"))
