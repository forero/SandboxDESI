import desisim.quicksurvey as qs

output_path = '/project/projectdirs/desi/users/forero/lowfat_lib/'
targets_path = '/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/'
fiberassign_exec = '/global/homes/f/forero/fiberassign/bin/./fiberassign'
epochs_path = '/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/'
template_fiberassign = 'template_fiberassign.txt'
setup = qs._sim_setup(output_path = output_path, 
                      targets_path = targets_path, 
                      fiberassign_exec = fiberassign_exec, 
                      epochs_path = epochs_path, 
                      template_fiberassign = template_fiberassign)

qs.create_directories(setup)


n_epochs = 5
epochs_list = range(n_epochs)

for epoch in epochs_list:
    qs.set_mtl_epochs(setup, epochs_list = epochs_list[epoch:])
    qs.set_fiber_epochs(setup, epochs_list = epochs_list[epoch])
    qs.create_surveyfile(setup)
    qs.create_fiberassign_input(setup)
    qs.simulate_epoch(setup, perfect=True)
