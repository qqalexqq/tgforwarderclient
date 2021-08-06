FROM python:3.9-slim

ADD requirements.txt ./
RUN pip install -r requirements.txt -U
ADD tg_forwarder_client.py ./
ADD export_session.py ./

CMD ["python", "tg_forwarder_client.py"]
