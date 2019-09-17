#!/bin/sh

#SBATCH --job-name=Data_Analysis_compiler

#SBATCH --array=1-3:1

#SBATCH --mem-per-cpu=1G   # Memory per core, use --mem= for memory per node
#SBATCH --time=23:00:00   # Use the form DD-HH:MM:SS
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

#SBATCH --mail-user=jwryan@phys.ksu.edu
#SBATCH --mail-type=ALL    # same as =BEGIN,FAIL,END

module load Anaconda3

python Mean_discrepancy_compiler.py $SLURM_ARRAY_TASK_ID
