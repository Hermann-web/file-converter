MODULE=./convcore

poetry run isort $MODULE
poetry run black $MODULE
# pylint $MODULE
poetry run flake8 $MODULE
