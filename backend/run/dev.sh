#!/bin/bash

echo "Starting FastAPI in development mode..."

# Load environment variables from .env file
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Run FastAPI with hot-reloading
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
