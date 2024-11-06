FROM python:3.9

WORKDIR /app

COPY main.py /app
COPY requirements.txt /app
COPY .env /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
