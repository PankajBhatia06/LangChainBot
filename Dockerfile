# MACOS
# FROM python:3.11-slim

# WINDOWS
FROM python:3.11-windowsservercore

WORKDIR /code

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

CMD ["streamlit", "run", "app.py"]