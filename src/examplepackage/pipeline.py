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
from examplepackage.features import my_feature_xxx,run_pipeline,convert_dcm2mif,concatenate




def main():
    directory = '/home/visionlab/Desktop/dMRI_data_harmonization'
    '''This function will explore the different folder inside the main path'''
    site_sub_files,output_mif = run_pipeline(directory)
    #print(output_mif)
    '''convert dcm to mif. The input are generated from the run_pipeline'''
    #convert_dcm2mif(site_sub_files,output_mif)
    '''Concatenate the different files for each subject into one single file'''
    list_dest_conc=concatenate(output_mif,directory)
    '''DENOISING'''





if __name__ == '__main__':
    main()




