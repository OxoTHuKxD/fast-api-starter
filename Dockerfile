FROM python:3.8-slim-buster

RUN mkdir /config
ADD requirements /config/
RUN pip install -r /config/requirements.txt

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /backend
EXPOSE 8000
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "src.main:app"]
ARG VERSION

ENV VERSION $VERSION

ADD alembic.ini /alembic.ini
ADD alembic /alembic
ADD src /backend/src
