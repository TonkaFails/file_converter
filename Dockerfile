FROM python:3.12.1-alpine

WORKDIR /

RUN apk add --no-cache ffmpeg
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]