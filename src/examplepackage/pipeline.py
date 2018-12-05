"""
This module should contain your main project pipeline(s).

Whilst the pipeline may change during the analysis phases, any more stable pipeline should be implemented here so
that it can be reused and easily reproduced.
"""
import pandas as pd
import os
from multiprocessing import Pool
import random
import string
import subprocess

from examplepackage import features
from examplepackage.i_o import IO
from examplepackage.examplemodule import hello_world
from examplepackage.features import my_feature_xxx,run_pipeline,convert_dcm2mif,concatenate,denoising,gibbs_ringing,preproc,mask,bias_correction



'''Be aware of using the same structure of the data tree'''


def main():
    directory = '/home/visionlab/Desktop/dMRI_data_harmonization'
    '''This function will explore the different folder inside the main path'''
    site_sub_files,output_mif = run_pipeline(directory)
    #print(output_mif)
    '''convert dcm to mif. The input are generated from the run_pipeline'''
    #convert_dcm2mif(site_sub_files,output_mif)

    '''Concatenate the different files for each subject into one single file'''
    flag=False #put true if you want run the bash command
    list_dest_conc=concatenate(output_mif,directory,flag)

    '''denoise the file contained in list_dest_conc'''
    flag_denoise=False
    list_dest_denoised=denoising(list_dest_conc,flag_denoise)

    "GIBBS"
    flag_gibbs = False
    list_dest_gibbs=gibbs_ringing(list_dest_denoised,flag_gibbs)

    "PREPROC"
    flag_preproc = False
    list_dest_preproc = preproc(list_dest_gibbs, flag_preproc)

    "MASKING"
    flag_mask=False
    list_dest_masked=mask(list_dest_preproc, flag_mask)

    "BIAS"
    flag_bias = True
    list_dest_bias = bias_correction(list_dest_masked, flag_bias)




if __name__ == '__main__':
    main()




