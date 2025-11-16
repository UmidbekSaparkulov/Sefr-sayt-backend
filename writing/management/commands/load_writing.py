import json
from django.core.management.base import BaseCommand
from writing.models import Writing

class Command(BaseCommand):
    help = "Load Writing data from JSON file into admin panel"

    def add_arguments(self, parser):
        parser.add_argument(
            "json_file",
            type=str,
            help="Path to JSON file with writing data"
        )

    def handle(self, *args, **options):
        json_file = options["json_file"]
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            count = 0
            for item in data:
                # Avtomatik yaratish yoki yangilash (title unikal asos)
                obj, created = Writing.objects.update_or_create(
                    title=item['title'],
                    defaults={
                        "type": item.get("type", ""),
                        "description": item.get("description", ""),
                        "themes": item.get("themes", []),
                    }
                )
                count += 1

            self.stdout.write(self.style.SUCCESS(f"{count} ta Writing yozuv admin panelga yuklandi ✅"))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {json_file}"))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f"Invalid JSON file: {json_file}"))
