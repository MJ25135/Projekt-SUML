FROM python:3.11

EXPOSE 8080
WORKDIR /pythonProject

COPY . ./

RUN pip install -r requirements.txt

CMD streamlit run --server.port 8080 --server.enableCORS false app.py
