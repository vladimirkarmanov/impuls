#!/bin/bash
python manage.py loaddata groups.json --settings=impuls.settings.development
python manage.py loaddata users.json --settings=impuls.settings.development
