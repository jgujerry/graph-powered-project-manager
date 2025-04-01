#!/bin/bash

echo "Starting FastAPI in production mode..."

# Set environment variables (if needed)
export FASTAPI_ENV=prod

# Start FastAPI with Gunicorn and Uvicorn workers
gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 app.main:app
