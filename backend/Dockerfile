FROM python:3.10
WORKDIR /app
COPY ./backend .
RUN pip install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000" ]
