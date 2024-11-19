FROM python:3.9-bullseye

WORKDIR /app/api

COPY build/requirements.txt .

# Install base requirements
RUN pip3 install -r requirements.txt

# Copy main files
COPY src/ ./src

# Change directory to src
WORKDIR /app/api/src/

RUN for plugin in /app/api/src/lib/*; do \
    if [ -d "$plugin" ] && [ -f "$plugin/requirements.txt" ]; then \
        echo "Installing dependencies for $plugin"; \
        pip install --no-cache-dir -r "$plugin/requirements.txt"; \
    fi \
done

# Run the server
CMD ["fastapi", "run"]