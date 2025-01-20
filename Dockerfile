FROM python:3.11

EXPOSE 8001
WORKDIR /pythonProject

COPY . ./

RUN pip install -r requirements.txt

CMD streamlit run --server.port 8001 --server.enableCORS false app.py
