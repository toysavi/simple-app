FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
