FROM python:3.9-buster

# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED=TRUE

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE=TRUE

RUN mkdir /finances_summary

COPY scripts/api-entrypoint-dev.sh /scripts/api-entrypoint-dev.sh
COPY src/finances_summary/ /finances_summary/
COPY /.env /.env
ENV PYTHONPATH=./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --requirement /finances_summary/requirements.txt

RUN chmod 774 /scripts/api-entrypoint-dev.sh
RUN chmod 774 /finances_summary -R

EXPOSE 8000

ENTRYPOINT [ "/scripts/api-entrypoint-dev.sh" ]