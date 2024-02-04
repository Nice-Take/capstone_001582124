#!/bin/bash

# Run Docker container in the background
docker run -p 8000:80 nicetake/estimator:latest &

# Wait for 2 seconds
sleep 4

# Open the HTML file in the default web browser
xdg-open "./estimator.html" || open "./estimator.html" || echo "Please open ./estimator.html in your web browser."
