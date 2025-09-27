FROM python:3.11.9

WORKDIR /app

COPY requirements.txt pyproject.toml ./

COPY prod_assistant ./prod_assistant

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "prod_assistant.router.main:app", "--host", "0.0.0.0", "--port", "8000"]