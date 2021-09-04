FROM python:3.9-buster

# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED=TRUE

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE=TRUE

RUN mkdir /finances_summary

COPY src/finances_summary/ /finances_summary/
RUN ls -la /finances_summary
# COPY scripts/entrypoint-dev.sh /finances_summary/entrypoint-dev.sh
# COPY certs/localhost+2.pem /localhost+2.pem
# COPY certs/localhost+2-key.pem /localhost+2-key.pem

ENV PYTHONPATH=./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --requirement /finances_summary/requirements.txt

RUN chmod 774 /finances_summary/scripts/entrypoint-dev.sh
RUN chmod 774 /finances_summary -R

EXPOSE 8000

ENTRYPOINT [ "/finances_summary/scripts/entrypoint-dev.sh" ]