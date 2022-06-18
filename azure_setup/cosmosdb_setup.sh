#!/usr/bin/bash

echo off
set -xeuo 
set pipefail -c

source variables.sh

# login to azure
az login

# Create cosmos db account
az cosmosdb create \
-n $cosmosDBAccountName \
-g $resourceGroupName \
--locations regionName=eastus \
--server-version 4.0 \
--kind MongoDB \
--enable-free-tier true \
--backup-redundancy Local
# --locations regionName=$location \

# Create database in cosmos db
az cosmosdb mongodb database create \
--account-name $cosmosDBAccountName \
--name $cosmosDBDatabaseName \
-g $resourceGroupName

# # Create advertisements collection
az cosmosdb mongodb collection create \
--account-name $cosmosDBAccountName \
--database-name $cosmosDBDatabaseName \
--name advertisements \
-g $resourceGroupName

# # Create posts collection
az cosmosdb mongodb collection create \
--account-name $cosmosDBAccountName \
--database-name $cosmosDBDatabaseName \
--name posts \
-g $resourceGroupName
