FROM python:3.9-bullseye

WORKDIR /app/api

COPY build/requirements.txt .

# Install base requirements
RUN pip3 install -r requirements.txt

# Copy main files
COPY src/ ./src

# Change directory to src
WORKDIR /app/api/src/

# Run the server
CMD ["fastapi", "run"]