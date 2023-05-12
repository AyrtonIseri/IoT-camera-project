#!/bin/bash

# Exit in case of execution fail
set -e

# Load environment variables from .env file
. ./.config/.env

while true
do
    # Loads new captures to the cloud and cleans the buffer
    python photo-dumper.py 'nema' '/var/www/html/uploads/'

    # Logs information to the console
    local_time=$(date +%H:%M:%S)
    string="Screened all photo dumper. Logged at $local_time"
    echo $string
    
    # Rests and waits for the queue to have something again
    sleep $COMPUTER_LISTENING_TIME_FREQ
done