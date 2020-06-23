#!/bin/bash
python manage.py loaddata groups.json --settings=backend.settings.development
python manage.py loaddata users.json --settings=backend.settings.development