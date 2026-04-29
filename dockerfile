FROM python:3.12-slim

# Evita prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/root/.local/bin:$PATH"

# Actualiza paquetes
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    curl \
    wget \
    vim \
    nano \
    build-essential \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /workspace

RUN pip install poetry

COPY poetry.lock .
COPY pyproject.toml .
COPY server.py .

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi



CMD ["python3", "server.py"]