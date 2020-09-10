#!/bin/bash
BASEDIR=$(dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd ))
docker run --rm --env-file ${BASEDIR}/.env \
    -v "${BASEDIR}/data:/src/data" \
    -v "${BASEDIR}/customer:/src/customer" \
    arcoro.azurecr.io/intechideas-team/onboarding-paycor--intechideas $@