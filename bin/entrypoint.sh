#! /usr/bin/env sh

# run all migrations
echo "run migrations..."
alembic upgrade head

# run server
echo "run app..."
uvicorn main:app --reload --host 0.0.0.0