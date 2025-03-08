#!/bin/bash
set -e  # Exit if any command fails

# Start the plugin handler (runs indefinitely due to `while True`)
poetry run python plugin_handler/main.py &

# Start FastAPI
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Keep the script alive
wait