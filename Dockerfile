FROM python:3.10.6
# Install dependencies
RUN pip install poetry rich
ENV PYTHONUNBUFFERED=1
COPY pyproject.toml /tmp 
COPY poetry.lock /tmp
RUN poetry config virtualenvs.create false
WORKDIR /tmp
RUN poetry install
RUN mkdir /app 
 COPY . /app
WORKDIR /app
