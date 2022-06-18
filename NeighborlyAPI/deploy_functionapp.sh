#!/usr/bin/bash

echo off
set -xeuo 
set pipefail -c

source ../azure_setup/variables.sh

# login to azure
az login

# Deploy function app
func \
    azure \
    functionapp \
    publish \
    $functionAppName
