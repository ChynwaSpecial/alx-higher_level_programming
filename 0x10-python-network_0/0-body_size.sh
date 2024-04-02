#!/bin/bash
# Send a request to the URL and get the size of the response body
size=$(curl -s -o /dev/null -w "%{size_download}" "$url")
