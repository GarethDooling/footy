
sudo apt update
sudo apt install python3-venv python3-pip python -y

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt