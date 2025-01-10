#!/bin/env bash

if [ $# -eq 2 ]; then
    start_day=$1
    end_day=$2
    for day in $(seq $start_day $end_day); do
        echo "Day : $day"
        mkdir -p $day
        echo "import os, sys
sys.path.append(os.path.abspath('../'))

import utils

def main():
    inputs = utils.read_inputs('i1')
    
if __name__ == '__main__':
    main()" >  $day/1.py
        echo "import os, sys
sys.path.append(os.path.abspath('../'))

import utils

def main():
    inputs = utils.read_inputs('i2')
    
if __name__ == '__main__':
    main()" >  $day/2.py
        touch $day/i{1..2}
        rm $day/{1..2}.input
    done
else
    echo 'Invalid Arguments'
    exit 1
fi