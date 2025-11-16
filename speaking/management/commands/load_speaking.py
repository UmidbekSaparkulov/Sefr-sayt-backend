import json
from django.core.management.base import BaseCommand
from speaking.models import TestInfo, TestTip, Expectation, SampleQuestion, SampleQuestionGuideline

class Command(BaseCommand):
    help = 'Load initial test data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path',
            type=str,
            help='The path to the JSON file containing test data'
        )

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # TestInfo
        test_info = data['testInfo']
        TestInfo.objects.update_or_create(
            id=1,
            defaults={
                "questions": test_info["questions"],
                "minutes": test_info["minutes"],
                "task_types": test_info["taskTypes"]
            }
        )

        # TestTips
        for tip in data['testTips']:
            TestTip.objects.update_or_create(text=tip)

        # Expectations
        for exp in data['expectations']:
            Expectation.objects.update_or_create(text=exp)

        # SampleQuestion
        sq_data = data['sampleQuestion']
        sq, created = SampleQuestion.objects.update_or_create(
            task_title=sq_data["taskTitle"],
            defaults={
                "image_url": sq_data["imageUrl"],
                "prompt": sq_data["prompt"],
                "preparation": sq_data["preparation"],
                "speaking": sq_data["speaking"]
            }
        )

        # Guidelines
        for g in sq_data['guidelines']:
            SampleQuestionGuideline.objects.update_or_create(
                sample_question=sq,
                text=g
            )

        self.stdout.write(self.style.SUCCESS('Test data loaded successfully!'))
