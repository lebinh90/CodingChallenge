#!/bin/bash

JSON_File="/PathTo/JSON/File"

cat ${JSON_File} | jq .five.six.seven
