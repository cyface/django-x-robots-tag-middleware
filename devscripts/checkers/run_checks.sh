#!/bin/bash
. .env/bin/activate
python manage.py jenkins --pylint-rcfile=devscripts/checkers/pylintrc --coverage-rcfile=devscripts/checkers/coveragerc --csslint-interpreter=node --csslint-implementation=/usr/bin/csslint --jslint-interpreter=node x_robots_tag_middleware