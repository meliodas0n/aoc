#!/bin/env bash

if [ $# -eq 2 ]; then
    start_day=$1
    end_day=$2
    for day in $(seq $start_day $end_day); do
        echo "Day : $day"
        mkdir -p $day
        touch $day/{1..2}.py
        touch $day/{1..2}.input
    done
else
    echo 'Invalid Arguments'
    exit 1
fi