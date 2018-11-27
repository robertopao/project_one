"""
This module should contain project specific feature engineering functionality.

You should avoid engineering features in a notebook as it is not transferable later if you want to automate the
process. Add functions here to create your features, such functions should include those to generate specific features
along with any more generic functions.

Consider moving generic functions into the shared statoilds package.
"""
import pandas as pd
import multiprocessing as mp
import random
import string
import os



def my_feature_xxx(df: pd.DataFrame):
    """
    Description goes here.
    You might also add additional arguments such as column etc...
    Would be nice with some test cases also :)

    Args:
        df: Dataframe upon which to operate

    Returns:
        A dataframe with the Xxx feature appended
    """

    # CODE HERE

    return df



def run_pipeline():
    """
    Run the main processing pipeline.

    Returns:
        A dataframe containing the output of the pipeline
    """

    # io = IO(path)
    # df = io.load_cleaned_file(download_always=False)
    # df = add_choke_events(df)

    # Add calls to features.Xxx here

    directory = '/home/visionlab/Desktop/dMRI_data_harmonization'
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
                site_sub_files[k]=site_dicom_sub[j]+'/'+another_file_1+'/'
                k=k+1
            j = j + 1
        i=i+1
    splitted={}
    output_mif={}
    for i in range (len(site_sub_files)):
        splitted[i]=site_sub_files[i].split('/')
        output_mif[i]=directory+'/'+splitted[i][5]+'/MIF-raw/'+splitted[i][5]+'_'+splitted[i][7]+'_'+splitted[i][9]+'.mif'


    # save (or return) dataframe here?
    return site_sub_files,output_mif

def convert_dcm2mif(site_sub_files,output_mif):
    for i in range(len(site_sub_files)):
        bashCommand = ("/home/visionlab/mrtrix3/bin/mrconvert " + site_sub_files[i]+" "+ output_mif[i])
        os.system(bashCommand)
    return

