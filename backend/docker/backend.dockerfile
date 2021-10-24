FROM python:3.10-buster

WORKDIR /app/

# Install Poetry
COPY ./requirements.txt /app/requirements.txt

# Allow installing dev dependencies to run tests
RUN pip install -r requirements.txt

COPY . /app
COPY bin/entrypoint.sh /entrypoint.sh

ENV PYTHONPATH=/app

RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]