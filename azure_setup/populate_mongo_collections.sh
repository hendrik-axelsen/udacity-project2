#!/usr/bin/bash

echo off
set -xeuo 
set pipefail -c

source variables.sh

mongoimport \
--uri $mongoDBConnectionString \
--db $cosmosDBDatabaseName \
--collection 'advertisements' \
--file='sample_data/sampleAds.json' \
--jsonArray

mongoimport \
--uri $mongoDBConnectionString \
--db $cosmosDBDatabaseName \
--collection 'posts' \
--file='sample_data/samplePosts.json' \
--jsonArray
