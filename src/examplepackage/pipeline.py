"""
This module should contain your main project pipeline(s).

Whilst the pipeline may change during the analysis phases, any more stable pipeline should be implemented here so
that it can be reused and easily reproduced.
"""
import pandas as pd
import os

from examplepackage import features
from examplepackage.i_o import IO
from examplepackage.examplemodule import  hello_world


def run_pipeline(local_data_path: object) -> object:
    """
    Run the main processing pipeline.

    Returns:
        A dataframe containing the output of the pipeline
    """

    # io = IO(path)
    # df = io.load_cleaned_file(download_always=False)
    # df = add_choke_events(df)

    # Add calls to features.Xxx here

    directory = '/home/visionlab/Desktop/dMRI data harmonization'
    site=os.listdir(directory)
    site_dicom={}
    site_dicom_sub={}
    site_sub_files={}
    i,k,j=0,0,0
    for filename in site:
        site_dicom[i]=directory+'/'+filename+'/DICOM-raw'
        temporary_path=os.listdir(site_dicom[i])

        for another_file in temporary_path:
            site_dicom_sub[j]=site_dicom[i]+'/'+another_file+'/scans'
            temporary_path_1 = os.listdir(site_dicom_sub[j])
            for another_file_1 in temporary_path_1:
                site_sub_files[k]=site_dicom_sub[j]+'/'+another_file_1
                k=k+1
            j = j + 1
        i=i+1
    splitted={}
    output_mif={}
    for i in range (len(site_sub_files)):
        splitted[i]=site_sub_files[i].split('/')
        output_mif[i]=directory+'/'+splitted[i][5]+'/MIF-raw/'+splitted[i][5]+'_'+splitted[i][7]+'_'+splitted[i][9]+'.mif'

    string_to_print=hello_world()
    print(string_to_print)
    print("hi")



    # save (or return) dataframe here?
    return string_to_print


okkkk=run_pipeline('/home/visionlab/Desktop/dati')