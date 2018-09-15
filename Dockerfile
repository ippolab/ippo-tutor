FROM python:3.7
ENV PYTHONBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD ./backend/Pipfile* /src/
RUN pip install pipenv && pipenv lock -r > requirements.txt && pip install -r requirements.txt
ADD ./backend /src/
