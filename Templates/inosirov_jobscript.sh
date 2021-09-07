#!/bin/bash
#----------------------------------------------------
# Ibrohim Nosirov Job Script
#
#   *** Serial Job on Normal Queue ***
# 
#
#----------------------------------------------------

#SBATCH -J ib_DLC_frame_extraction           # Job name
#SBATCH -o logs/ib_DLC_frame_extraction.o%j       # Name of stdout output file
#SBATCH -e logs/ib_DLC_frame_extraction.e%j       # Name of stderr error file
#SBATCH -p gtx          # Queue (partition) name
#SBATCH -N 1               # Total # of nodes (must be 1 for serial)
#SBATCH -n 1               # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 08:30:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=inosirov1024@gmail.com
#SBATCH --mail-type=all    # Send email at begin and end of job

module unload xalt
module load cuda/10.0
module load nccl
module load cudnn
module load tacc-singularity
module list 
pwd

# Launch serial code...
singularity exec --nv /work2/08229/inosirov/maverick2/DLCv2/deeplabcut_2_2_0_1.sif python3 dlc_functions.py
# ---------------------------------------------------
