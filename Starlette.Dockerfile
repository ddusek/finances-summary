FROM python:3.9-buster

# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED=TRUE

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE=TRUE

RUN mkdir /finances_summary

COPY scripts/starlette-entrypoint-dev.sh /scripts/starlette-entrypoint-dev.sh
COPY src/finances_summary/user /finances_summary/user
COPY src/finances_summary/certs /
COPY src/finances_summary/__init__.py /finances_summary/__init__.py
COPY src/finances_summary/settings.py /finances_summary/settings.py
COPY src/finances_summary/app.py /finances_summary/app.py
COPY /.env /.env
COPY src/finances_summary/requirements.txt /finances_summary/requirements.txt

ENV PYTHONPATH=./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --requirement /finances_summary/requirements.txt

RUN chmod 774 /scripts/starlette-entrypoint-dev.sh
RUN chmod 774 /finances_summary -R

EXPOSE 8000

ENTRYPOINT [ "/scripts/starlette-entrypoint-dev.sh" ]