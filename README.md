# ИСПОЛЬЗОВАНИЕ GIT-HOOKS

pip install pre-commit

## Prepare-Commit-Msg
pre-commit install --hook-type prepare-commit-msg

## Pre-Commit
...

## Pre-Push
pip install --user pipenv

### Init the virtual environment
pipenv install --dev pre-commit Commitizen toml
pipenv run cz init
pre-commit autoupdate
pipenv run cz bump

## Дополнительные источники / Полезные ссылки
https://dev.to/jalvaradosegura/create-your-own-pre-commit-hook-3kh
https://stackoverflow.com/questions/59499061/how-to-run-custom-shell-script-file-before-pre-commit-hook
https://habr.com/ru/companies/2gis/articles/838966/
https://pre-commit.com/#plugins
https://github.com/compilerla/conventional-pre-commit