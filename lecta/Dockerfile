FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

RUN --mount=type=cache,target=/root/.cache/pip pip install --upgrade pip && pip install -r requirements.txt

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD "/entrypoint.sh"