# python:alpine is 3.{latest}
FROM arcoro.azurecr.io/intechideas-team/onboarding-paycor--core

LABEL MAINTAINER="Erick Agrazal erick@agrazal.com"

COPY ./customer/ /src/customer/
COPY ./data/ /src/data

