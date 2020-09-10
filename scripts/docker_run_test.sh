#!/bin/bash
docker run --dns=8.8.8.8 --rm  \
    -v "$(pwd)/tests:/src/tests"  \
    -v "$(pwd)/data:/src/data" \
    arcoro.azurecr.io/intechideas-team/onboarding-paycor--intechideas  nosetests --verbosity=2 tests/onboarding_ultimatepro_test.py:OnboardingUltimateproTest
