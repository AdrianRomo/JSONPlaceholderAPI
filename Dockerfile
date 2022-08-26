# We use Python 3.10
FROM python:3.10-alpine

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED 1

# Install system requirements
RUN apk update \
  # Python 3 dev dependencies
  && apk add --virtual build-deps gcc git make linux-headers python3-dev \
  musl-dev libffi-dev openssl-dev g++ \
  # Upgrade pip
  && pip install --upgrade pip

# Set the workdir as /app
WORKDIR /app

# Copy the requirements.txt
COPY ./source/requirements.txt /app/source/requirements.txt

# Install python programmer-defined dependencies
RUN pip install -r source/requirements.txt

# Install gunicorn to run the application in production
RUN pip install uvicorn

# Copy the entire source for the application
COPY ./source/ /app

EXPOSE 5000

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec uvicorn --host "0.0.0.0" --port "5000" --workers 1 source.main:app