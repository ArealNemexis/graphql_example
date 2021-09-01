FROM python:3.9-slim

ENV TZ=America/Sao_Paulo

COPY setup.py /deploy/

COPY graphql_fastapi /deploy/graphql_fastapi

WORKDIR /deploy

RUN pip install .

CMD ["uvicorn", "graphql_fastapi:app", "--port", "8000", "--host", "0.0.0.0"]