FROM python:3.12-slim-bullseye


# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev \
    cargo \
    git \
    bash \
    && rm -rf /var/lib/apt/lists/* \

# Create non-root user
RUN groupadd --gid ${GID} ${USER} && \
    useradd --uid ${UID} --gid ${GID} --shell /bin/bash --create-home ${USER} \

# Set working directory
WORKDIR /home/${USER}/app

# Create writable media directory
RUN mkdir -p /home/${USER}/media && \
    chown -R ${USER}:${USER} /home/${USER}/media && \
    chmod -R 777 /home/${USER}/media \

# Copy project files with proper ownership
COPY --chown=${USER}:${USER} ./task_manager ./task_manager
COPY --chown=${USER}:${USER} ./entrypoint.sh .
COPY --chown=${USER}:${USER} ./poetry.lock ./pyproject.toml ./

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Install Poetry and dependencies
RUN pip install --upgrade pip setuptools wheel poetry && \
    poetry install --no-ansi

# Switch to non-root user
USER ${USER}
