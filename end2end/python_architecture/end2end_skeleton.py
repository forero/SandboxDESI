import desitarget.mtl as mtl
import desisim.quickcat as qc
import desisim.quicksurvey as qs 


survey_setup = qs.survey_setup()

for layer in survey_setup.layers():
    layer_targets = mtl.setup_targets(survey_setup = survey_setup)

    layer_assignments = qs.assignfiber(survey_setup = survey_setup, 
                                       targets = layer_targets) 

    layer_redshiftcat = qc.getredshift(survey_setup = survey_setup, 
                                       targets = layer_targets, 
                                       assignments = layer_assignments)

    survey_setup.status_update(targets=layer_targets, 
                               assignments=layer_assignments, 
                               redshiftcat=layer_redshiftcat)
    
qs.evaluate_survey(survey_setup = survey_setup)
