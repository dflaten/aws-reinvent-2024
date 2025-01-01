FROM public.ecr.aws/lambda/python:3.11 as builder

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Copy dependency files
COPY pyproject.toml uv.lock ${LAMBDA_TASK_ROOT}/

# Install dependencies using uv sync with lockfile
RUN /root/.cargo/bin/uv sync \
    --lockfile ${LAMBDA_TASK_ROOT}/uv.lock \
    --target "${LAMBDA_TASK_ROOT}" \
    --cache-dir=/tmp/uv-cache

# Runtime stage
FROM public.ecr.aws/lambda/python:3.11-slim

# Copy dependencies from builder
COPY --from=builder ${LAMBDA_TASK_ROOT} ${LAMBDA_TASK_ROOT}

# Copy application code
COPY app.py ${LAMBDA_TASK_ROOT}

# Set environment variables
ENV PYTHONPATH="${LAMBDA_TASK_ROOT}"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the CMD to your handler
CMD [ "app.handler" ]
