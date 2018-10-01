FROM python:3.7
ENV PYTHONBUFFERED 1
RUN mkdir /src
WORKDIR /src
COPY Pipfile* /src/
RUN pip install pipenv && \
    pipenv lock -r > requirements.txt && \
    pip install -r requirements.txt
ADD . /src/
RUN cp /src/config/settings.py /src/ippo_tutor/
CMD python manage.py migrate && gunicorn ippo_tutor.wsgi -b 0.0.0.0:8000 -w 4
