#! /bin/bash
if [ ! -d "/opt/tornado-teaching" ]; then 
    echo "Creating virtual environment"
    pushd /opt
    virtualenv tornado-teaching
    popd
fi
source /opt/tornado-teaching/bin/activate
HAS_TORNADO=$(pip list | grep tornado)
echo "Test for tornado found: ${HAS_TORNADO}"
if [ -z "$HAS_TORNADO" ]; then
    echo "Installing tornado"
    pushd /opt
    pip install tornado
    popd
fi
