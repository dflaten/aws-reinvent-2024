FROM public.ecr.aws/lambda/python:3.12

# Install tar and other required tools
COPY --from=ghcr.io/astral-sh/uv:0.5.17 /uv /bin/uv

ENV UV_CACHE_DIR=/tmp/.uv_cache

# Copy dependency files
COPY pyproject.toml .
COPY uv.lock .
COPY handler.py .

# Install dependencies using uv sync with lockfile
RUN uv pip install --system -Ue .
# This verifies the function has all the dependencies it needs to run.
RUN python3 handler.py

# Set the CMD to your handler
CMD [ "handler.lambda_handler" ]
