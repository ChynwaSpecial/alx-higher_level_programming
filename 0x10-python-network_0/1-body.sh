#!/bin/bash
# Get the URL from the argument
url=$1

# Send a GET request to the URL and display the body if the status code is 200
response=$(curl -s -w "%{http_code}" -o temp.txt "$url")
status_code=$(tail -n1 temp.txt)
if [ "$status_code" = "200" ]; then
    cat temp.txt
else
    echo "Status code: $status_code"
