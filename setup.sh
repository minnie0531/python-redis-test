#/bin/bash

# Check if windows or linux

os=`uname -s`
echo $os

echo "Current system is Linux"
echo "Install vitual environment"
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
cp hooks/pre-commit.py .git/hooks/pre-commit
