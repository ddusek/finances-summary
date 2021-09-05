FROM node:latest

RUN mkdir frontend

COPY src/frontend/src /frontend/src
COPY src/frontend/package.json /frontend/package.json
COPY src/frontend/package-lock.json /frontend/package-lock.json
# COPY frontend/vue.config.js /app/vue.config.js
COPY scripts/frontend-entrypoint.sh /scripts/frontend-entrypoint.sh
# COPY certs/localhost+2.pem /app/localhost+2.pem
# COPY certs/localhost+2-key.pem /app/localhost+2-key.pem

RUN chmod 774 /scripts/frontend-entrypoint-dev.sh

WORKDIR /frontend/
RUN npm i

EXPOSE 8080

ENTRYPOINT [ "/scripts/frontend-entrypoint-dev.sh" ]