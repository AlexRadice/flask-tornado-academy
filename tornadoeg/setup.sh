#! /bin/bash
if [ ! -d "/opt/tornado-teaching" ]; then 
    echo "Creating virtual environment"
    pushd /opt
    virtualenv tornado-teaching
    popd
fi
source /opt/tornado-teaching/bin/activate
pip install -r requirements.txt
