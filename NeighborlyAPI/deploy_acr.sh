#!/usr/bin/bash

echo off
set -xeuo 
set pipefail -c

source ../azure_setup/variables.sh

# login to azure
az login

# Create acr
az acr create \
  --resource-group $resourceGroup \
  --name $containerRegistry \
  --sku Basic

# Login to acr
az acr login \
  --name $containerRegistry

