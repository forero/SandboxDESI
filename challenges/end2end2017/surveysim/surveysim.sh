#!/bin/bash
#############################################################################
# Example automation for cycling between surveyplan and surveysim using
# a greedy scheduling algorithm for the next tile selector. Since the
# greedy scheduler does not use hour-angle assignments, surveyplan is
# relatively fast since no hour-angle optimization is required. The total
# time to run a 5-year survey with this script is about 45 minutes.
#############################################################################

PLAN_ARGS='--verbose --nopt 0'
SIM_ARGS='--verbose --seed 123 --strategy HA+fallback --plan plan.fits'

export DESISURVEY=$PWD/output
export SURVEYPLAN=surveyplan
export SURVEYSIM=surveysim
surveyplan --create ${PLAN_ARGS}
surveysim ${SIM_ARGS}

while :
do
    (surveyplan ${PLAN_ARGS}) || break
    (surveysim --resume ${SIM_ARGS}) || break
done