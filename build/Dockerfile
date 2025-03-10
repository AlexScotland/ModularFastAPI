# Stage 1: Build the dependencies
FROM python:3.9-bullseye AS builder

WORKDIR /app/api

# Install Poetry
RUN pip3 install poetry

# Copy only the dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --without dev --no-root

# Install Watchdog for auto discovery
RUN poetry add watchdog

# Stage 2: Build the final image

FROM builder AS final

WORKDIR /app

# Copy the installed dependencies from the builder stage
COPY --from=builder /app/api /app/api

# Copy the rest of the application code
COPY . .

# Set the working directory
WORKDIR /app/api/modular-fastapi

# Run the server
CMD ["bash", "./start.sh"]
