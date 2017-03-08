#!/bin/sh
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
echo $SCRIPT_DIR
python2 ${SCRIPT_DIR}/app.py
