FROM python:3.9-bullseye

WORKDIR /app/api

COPY build/requirements.txt .

# Install base requirements
RUN pip3 install -r requirements.txt

# Copy main files
COPY . .

# Change directory to src
WORKDIR /app/api/modular_fastapi/

# Run the server
CMD ["fastapi", "run"]