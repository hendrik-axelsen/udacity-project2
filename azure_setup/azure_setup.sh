#!/usr/bin/bash

echo off
set -xeuo 
set pipefail -c

source variables.sh

# login to azure
az login

# Create resource group
az group create \
-l $location \
-n $resourceGroupName

# Create storage account
az storage account create \
-n $storageAccountName \
-g $resourceGroupName \
-l $location \
--sku Standard_LRS \
--access-tier Cool \

# Create function app
az functionapp create \
-n $functionAppName \
-g $resourceGroupName \
-s $storageAccountName \
--runtime Python \
--runtime-version 3.9 \
--consumption-plan-location $location \
--os-type Linux \
--functions-version 4
