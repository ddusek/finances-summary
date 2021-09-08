#!/usr/bin/env bash

GREEN=$(tput setaf 2)
NORMAL=$(tput sgr0)

# check if node is installed
printf "\n${GREEN}Check if nodejs is installed, which is needed for Pyright.${NORMAL}\n"
# command -v node >/dev/null 2>&1 || { echo >&2 "Nodejs not installed. Aborting."; exit 1; }
if ! command -v node &> /dev/null; then
    echo "Nodejs is not installed, install it first."
    exit 1
else
    echo "Nodejs is installed, checking version..."
fi

# check node version
node_version="$(node -v)"
required_verson="14.0.0"
if [ "$(printf '%s\n' "$required_verson" "${node_version//v}" | sort -V | head -n1)" = "$required_verson" ]; then 
    echo "node version is fine ${required_verson}"
else
    echo "Node version is not sufficient. ${required_verson} or above is required."
    exit 1
fi

# check if pyright is installed
printf "\n${GREEN}Check if Pyright is installed.${NORMAL}\n"
if ! command -v pyright &> /dev/null; then
    echo "Pyright is not installed, installing now..."
    npm i -g pyright
else
    echo "Pyright is installed."
fi

# generate type stubs for Pyright
printf "\n${GREEN}Generating Type Stubs...${NORMAL}\n"
pyright --createstub pymongo
pyright --createstub uvicorn

# generate dir for logging
printf "\n${GREEN}Generating folder for logging...${NORMAL}\n"
mkdir ../src/finances_summary/logs