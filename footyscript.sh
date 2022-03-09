#!/bin/bash

export DATABASE_URI=sqlite:///data.db

sudo apt update
sudo apt install python3-venv python3-pip python -y

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 -m pytest \
	--cov=application \
    --cov-report term-missing \

if [ $CREATE_SCHEMA == "true" ]
then
python3 create.py
fi

python3 app.py
