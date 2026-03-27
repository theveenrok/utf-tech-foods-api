set shell := ["bash", "-eu", "-o", "pipefail", "-c"]
set dotenv-load := true

VENV_DIR := ".venv"
CACHE_DIR := ".cache"

APP_HOST := env("APP_HOST", "127.0.0.1")
APP_PORT := env("APP_PORT", "8000")

default:
    @just --list

venv:
    @uv venv {{ VENV_DIR }}

sync:
    @uv sync --all-extras --all-groups

setup: venv sync
    @uv run --group="git-hooks" prek install

clean:
    @find -type d -name "dist" -exec rm -rf {} +
    @find -type d -name "{{ CACHE_DIR }}" -exec rm -rf {} +
    @find -type d -name "__pycache__" -exec rm -rf {} +
    @find -type d -name "*.egg-info" -exec rm -rf {} +
    @find -type f -name ".coverage" -exec rm -rf {} +
    @find -type f -name "*,cover" -exec rm -rf {} +
    @find -type f -name "*~" -exec rm -rf {} +
    @find -type f -name "*.egg" -exec rm -rf {} +

upgrade:
    @uv lock --upgrade
    @uv run --group="git-hooks" prek auto-update

lock:
    @uv lock

test:
    @uv run python manage.py test


migrate:
    @uv run python manage.py migrate

make-migrations:
    @uv run python manage.py makemigrations

app-serve:
    @uv run python manage.py runserver {{ APP_HOST }}:{{ APP_PORT }}
