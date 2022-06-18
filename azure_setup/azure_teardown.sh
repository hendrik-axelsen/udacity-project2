#!/usr/bin/bash

echo off
set -xeuo 
set pipefail -c

source variables.sh

# login to azure
az login

# Delete resource group
az group delete \
-n $resourceGroupName \
--yes