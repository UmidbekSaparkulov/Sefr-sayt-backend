

# SEFR Test Platform - Backend

Django REST Framework bilan yaratilgan test platforma backend.

## Features

- CRUD for Speaking, Listening, Reading, Writing tests
- Nested serializers (questions → options)
- Admin panel for managing tests
- API endpoints ready for frontend fetch

## Models Overview

### Speaking
- `TestInfo`, `TestTip`, `Expectation`
- `SampleQuestion`, `SampleQuestionGuideline` (nested)

### Reading
- `ReadingTest`, `Question`, `Option`
- `Segment`, `Paragraph`, `Heading` (nested)

### Listening
- `ListeningTest`, `ListeningQuestion`, `ListeningOption`

### Writing
- `WritingTest`, `WritingQuestion`, `WritingOption`

## Installation

```bash
git clone git@github.com:USERNAME/REPO_NAME.git
cd REPO_NAME
python -m venv myvenv
source myvenv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
