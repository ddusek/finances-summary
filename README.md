# Finances summary
App is in development and not yet ready.  
App for tracking investments and viewing price changes graphs.  
Comparison of specific buy gains/loses versus same buys but with DCA, etc...

## Development
App uses Uvicorn to run api, which is built on Starlette framework with MongoDB as database.  
FE is written in React with typescript.
### How to run dev
```
docker-compose --file docker-compose-dev.yaml up --build
```
