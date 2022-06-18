#!/usr/bin/bash

echo off
set -xeuo 
set pipefail -c

source variables.sh

# List the connection strings
az cosmosdb keys list \
--type connection-strings \
-g $resourceGroupName \
-n $cosmosDBAccountName \
| ./extract_connection_string.py
