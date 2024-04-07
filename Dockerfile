FROM python:3.12-bookworm

RUN pip install poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY poetry.lock pyproject.toml .env ./
RUN poetry install --only main --no-root && rm -rf $POETRY_CACHE_DIR

COPY src ./src
RUN poetry install --only main

ENTRYPOINT ["python", "-m", "poetry", "run", "./src/main.py"]