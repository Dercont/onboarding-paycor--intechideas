#!/bin/bash
###########################
# Script Variables ########
###########################
DOCKER_IMAGE=arcoro.azurecr.io/intechideas-team/onboarding-paycor--intechideas

##########################
# Script logic ###########
##########################
docker push $DOCKER_IMAGE
