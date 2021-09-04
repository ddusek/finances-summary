FROM node:latest

RUN mkdir frontend

COPY frontend/src /frontend/src
COPY frontend/package.json /frontend/package.json
COPY frontend/package-lock.json /frontend/package-lock.json
# COPY frontend/vue.config.js /app/vue.config.js
COPY scripts/frontend-entrypoint.sh /frontend/frontend-entrypoint.sh
# COPY certs/localhost+2.pem /app/localhost+2.pem
# COPY certs/localhost+2-key.pem /app/localhost+2-key.pem

RUN chmod 774 /frontend/entrypoint-dev.sh

WORKDIR /frontend/
RUN npm i

EXPOSE 8080

ENTRYPOINT [ "/frontend/entrypoint-dev.sh" ]