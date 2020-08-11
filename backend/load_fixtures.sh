#!/bin/bash
python manage.py loaddata groups.json --settings=config.settings.development
python manage.py loaddata users.json --settings=config.settings.development
