FROM python:3.9.13

ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_NO_INTERACTION=1

RUN pip install "poetry==1.1.14" -U
ADD pyproject.toml poetry.lock ./
RUN poetry install --no-dev
ADD tgforwarderclient/ /tgforwarderclient

ENTRYPOINT ["python", "-m", "tgforwarderclient"]
