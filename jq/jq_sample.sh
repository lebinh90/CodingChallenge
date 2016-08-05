#!/bin/bash

JSON_File="/PathTo/JSON/File"

get_seven=".five.six.seven"

cat ${JSON_File} | jq ${get_seven}
