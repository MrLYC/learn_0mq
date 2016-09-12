#!/bin/bash

function run_in_background() {
    python $@ &
    export JOBS="$! ${JOBS}"
}

function terminal_jobs() {
    if [[ "" != "${JOBS}" ]]; then
        kill -9 ${JOBS} >/dev/null 2>&1
    fi
}

trap "terminal_jobs" INT

export params_length=$#
for params in "$@"; do
    run_in_background ${params}
done

read
terminal_jobs

