FROM public.ecr.aws/lambda/python:3.12

# Install tar and other required tools
RUN microdnf install -y tar gzip
# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv /root/.local/bin/uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ${LAMBDA_TASK_ROOT}/

# Install dependencies using uv sync with lockfile
RUN cd ${LAMBDA_TASK_ROOT} && uv sync

# Copy application code
COPY handler.py ${LAMBDA_TASK_ROOT}

# Set environment variables
ENV PYTHONPATH="${LAMBDA_TASK_ROOT}"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the CMD to your handler
CMD [ "handler.lambda_handler" ]
