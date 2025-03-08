FROM python:3.9-bullseye

WORKDIR /app/api

# Install Poetry
RUN pip3 install poetry

# Copy main files
COPY . .

# Change directory to src
WORKDIR /app/api/modular-fastapi/
# Generate poetry.lock inside the container
RUN poetry lock

# Install core dependencies
RUN poetry install --without dev --no-root

# Install Watchdog for auto discovery
RUN poetry add watchdog

# Run the server
CMD ["bash", "./start.sh"]