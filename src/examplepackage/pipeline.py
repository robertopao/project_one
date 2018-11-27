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
from examplepackage.features import my_feature_xxx,run_pipeline,convert_dcm2mif




def main():
    site_sub_files,output_mif = run_pipeline()

    print(output_mif)
    convert_dcm2mif(site_sub_files,output_mif)



if __name__ == '__main__':
    main()




