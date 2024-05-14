#!/bin/bash

token=$1
chatid=$2

# newPhrase=$(python3 wordeli.py)
newPhrase=$(/usr/local/bin/python3 /wordeli/wordeli.py)

echo ""
echo $newPhrase

curl -X POST "https://api.telegram.org/$1/sendMessage" -d "chat_id=$2&text=$newPhrase"
