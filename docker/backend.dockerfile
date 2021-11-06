FROM python:3.10-buster

WORKDIR /app/

# Install Poetry
COPY ./src/requirements.txt /app/requirements.txt

# Allow installing dev dependencies to run tests
RUN pip install -r requirements.txt

COPY src/ /app
COPY bin/entrypoint.sh /entrypoint.sh

ENV PYTHONPATH=/app

RUN chmod +x /entrypoint.sh

CMD [ "/entrypoint.sh" ]