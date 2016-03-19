import desisim.quicksurvey as qs

output_path = '/project/projectdirs/desi/users/forero/lowfat_lib/'
targets_path = '/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/'
fiberassign_exec = '/global/homes/f/forero/fiberassign/bin/./fiberassign'
epochs_path = '/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/'
template_fiberassign = 'template_fiberassign.txt'
n_epochs = 5

setup = qs.SimSetup(output_path = output_path, 
                    targets_path = targets_path, 
                    fiberassign_exec = fiberassign_exec, 
                    epochs_path = epochs_path, 
                    template_fiberassign = template_fiberassign, 
                    n_epochs = n_epochs)

qs.simulate_setup(setup)

