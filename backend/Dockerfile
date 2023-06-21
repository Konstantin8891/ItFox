FROM python:3.10
WORKDIR /app
COPY ./backend .
RUN pip install -r app/requirements.txt --no-cache-dir
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000" ]
