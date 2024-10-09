FROM python:3.9-slim
WORKDIR /app
COPY assignment5script.py .
CMD ["python", "assignment5script.py"]
