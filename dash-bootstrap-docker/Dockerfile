FROM python:3.9
LABEL maintainer "Yunindyo Prabowo <yunindyo.prabowo@gmail.com>"
WORKDIR /code
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY ./ ./
ENV ENVIRONMENT_FILE=".env"

EXPOSE 8050
ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "index:server"]

# CMD ["python", "./index.py", "--host", "0.0.0.0"]