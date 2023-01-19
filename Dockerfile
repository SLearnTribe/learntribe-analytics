FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

#RUN apt-get install -y --no-install-recommends build-essential
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY . /app
WORKDIR /app

#RUN python -m venv ./venv
#ENV PATH="/venv/bin:$PATH"

RUN pip install -r requirements.txt

#EXPOSE 15351

ENTRYPOINT [ "python" ]

CMD ["main.py"]