FROM python:3.8
ENV PYTHONUNBEFFERED=1
WORKDIR /api
COPY requirements.txt /api/
RUN pip install -r requirements.txt
COPY . /api/