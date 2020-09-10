#!/bin/bash
###########################
# Script Variables ########
###########################
DOCKER_IMAGE=arcoro.azurecr.io/intechideas-team/onboarding-paycor--intechideas


##########################
# Script logic ###########
##########################
for i in "$@"; do
    case $i in
        -c=*|--ci=*)
        CI_BUILD="${i#*=}"
        ;;
        *)
        # unknown option
        ;;
    esac
done
if [ $CI_BUILD ]; then
    docker build --tag $DOCKER_IMAGE .
else
    DIR="../onboarding-paycor--core"
    CWD=$(pwd)
    if [ -d "$DIR" ]; then
        cd "$DIR"
        ./scripts/docker_build.sh
        cd "$CWD"
        docker build --tag $DOCKER_IMAGE .
    else
        echo "ERROR: This project must be stay with core project."
        exit 1;
    fi
fi