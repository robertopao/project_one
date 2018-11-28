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



def run_pipeline(directory):
    """
    Run the main processing pipeline.

    Returns:
        A dataframe containing the output of the pipeline
    """

    # io = IO(path)
    # df = io.load_cleaned_file(download_always=False)
    # df = add_choke_events(df)

    # Add calls to features.Xxx here

    #directory = main_directory
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



def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list







def concatenate(output_mif,directory):
    site=os.listdir(directory)
    site_mif = {}
    site_mif_files = {}
    site_mif_name={}
    site_DTI={}

    i, k, j = 0, 0, 0
    for filename in site:
        site_mif[i] = directory + '/' + filename + '/MIF-raw'
        site_DTI[i] = directory + '/' + filename + '/DTI-conc'
        temporary_path = os.listdir(site_mif[i])
        for another_file in temporary_path:
            site_mif_files[k] = site_mif[i] + '/' + another_file
            site_mif_name[k] = another_file
            k = k + 1
        i = i + 1


    #site_mif_files[0].split('/')[-1].split('_')[1]

    site_mif_name_lst=list(site_mif_name.values())
    indices={}
    indices_1=list()
    for k in range (len(site_mif_name)):
        indices[k] = [i for i, s in enumerate(site_mif_name_lst) if site_mif_files[k].split('/')[-1].split('_')[1] in s]
        temp=[i for i, s in enumerate(site_mif_name_lst) if site_mif_files[k].split('/')[-1].split('_')[1] in s]
        indices_1.append(temp)



    #[value for value in indices if value != indices[0]]
    single_index={}
    j=0
    while True:
        single_index[j]=indices_1[0]
        indices_1 =  [x for x in indices_1 if x != indices_1[0]]
        j=j+1
        if len(indices_1)==0:
            break


    #destination_con={}
    list_dest_conc=list()
    for item in single_index:
        single_index[item]
        s="/"
        seq=site_mif_files[single_index[item][0]].split('/')
        temp_0=s.join(seq[0:6])+'/DTI-conc/'
        temp = site_mif_name[single_index[item][0]]
        temp_1=temp.split('_')[0]+'_'+temp.split('_')[1]+"_DTI.mif"
        destination_conc=temp_0+temp_1
        list_dest_conc.append(destination_conc)
        bashCommand =("mrcat -axis  3 -force " + site_mif_files[single_index[item][0]] +" "+ site_mif_files[single_index[item][1]]+" "+site_mif_files[single_index[item][2]]+" "+ site_mif_files[single_index[item][3]]+" "+  destination_conc)
        os.system(bashCommand)
    return list_dest_conc

