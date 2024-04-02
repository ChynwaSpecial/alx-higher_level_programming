#!/bin/bash
# Send a GET request to the URL and display the body if the status code is 200
response=$(curl -s -w "%{http_code}" -o temp.txt "$url")status_code=$(tail -n1 temp.txt)
