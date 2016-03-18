import desisim.quicksurvey as qs

output_path = '/project/projectdirs/desi/users/forero/lowfat/'
targets_path = '/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/'
fiberassign_exec = '/global/homes/f/forero/fiberassign/bin/./fiberassign'
epochs_path = '/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/'
setup = qs._sim_setup(output_path = output_path, 
                      targets_path = targets_path, 
                      fiberassign_exec = fiberassign_exec, 
                      epochs_path = epochs_path)


