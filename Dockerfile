FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# RUN apt-get install -y --no-install-recommends build-essential
RUN apt-get update

RUN mkdir /app
COPY . /app
WORKDIR /app

#RUN python -m venv ./venv
#ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# Production
CMD ["gunicorn", "-c", "gunicorn.conf", "main:app"]
# Development
# ENTRYPOINT [ "python" ]
# CMD ["main.py"]