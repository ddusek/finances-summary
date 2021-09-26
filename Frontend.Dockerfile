FROM node:latest

RUN mkdir frontend

COPY src/frontend/src /frontend/src
COPY src/frontend/public /frontend/public
COPY src/frontend/package.json /frontend/package.json
COPY src/frontend/package-lock.json /frontend/package-lock.json
COPY src/frontend/.env /frontend/.env
COPY scripts/frontend-entrypoint-dev.sh /scripts/frontend-entrypoint-dev.sh
COPY src/frontend/secrets/0.0.0.0.pem /frontend/secrets/0.0.0.0.pem
COPY src/frontend/secrets/0.0.0.0-key.pem /frontend/secrets/0.0.0.0-key.pem

RUN chmod 774 /scripts/frontend-entrypoint-dev.sh

WORKDIR /frontend/
RUN npm i

EXPOSE 8080

ENTRYPOINT [ "/scripts/frontend-entrypoint-dev.sh" ]