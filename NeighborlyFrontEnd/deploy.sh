#!/usr/bin/bash

echo off
set -xeuo 
set pipefail -c

source ../azure_setup/variables.sh

# login to azure
az login

# Deploy web app
az webapp up \
    --runtime 'PYTHON:3.9' \
    --sku F1 \
    --logs \
    -l $location \
    -n $webAppName \
    -g $resourceGroupName
