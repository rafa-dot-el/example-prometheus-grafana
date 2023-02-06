FROM python:3.10-slim

COPY ./pyproject.toml /backend/pyproject.toml
COPY ./poetry.lock /backend/poetry.lock

WORKDIR /backend

RUN apt-get update && apt-get install -y build-essential && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install && \
    apt-get remove -y build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY ./backend /backend

EXPOSE 3001

CMD ["python", "backend.py"]
