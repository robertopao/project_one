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







def concatenate(output_mif,directory,flag):
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
        if flag == True:
            bashCommand =("mrcat -axis  3 -force " + site_mif_files[single_index[item][0]] +" "+ site_mif_files[single_index[item][1]]+" "+site_mif_files[single_index[item][2]]+" "+ site_mif_files[single_index[item][3]]+" "+  destination_conc)
            os.system(bashCommand)

    return list_dest_conc

def denoising(list_dest_conc,flag_denoise):
    list_dest_denoised=list()
    for i in range (len(list_dest_conc)):
        s = "/"
        seq = list_dest_conc[i].split('/')
        temp = s.join(seq[0:6])+'/DTI-denoised/'
        temp_1=list_dest_conc[i].split('/')[-1].split('.')[0]+'_denoised.mif'
        destination_denoised = temp + temp_1
        list_dest_denoised.append(destination_denoised)
        if flag_denoise == True:
            bashCommand =("dwidenoise "+list_dest_conc[i]+' ' +destination_denoised)
            os.system(bashCommand)
    return list_dest_denoised


def gibbs_ringing(list_dest_denoise,flag_gibbs):
    list_dest_gibbs=list()
    for i in range (len(list_dest_denoise)):
        s = "/"
        seq = list_dest_denoise[i].split('/')
        temp = s.join(seq[0:6])+'/DTI-gibbs/'
        temp_1=list_dest_denoise[i].split('/')[-1].split('.')[0]+'_gibbs.mif'
        destination_gibbs = temp + temp_1
        list_dest_gibbs.append(destination_gibbs)
        if flag_gibbs == True:
            bashCommand =("mrdegibbs "+list_dest_denoise[i]+' ' +destination_gibbs)
            os.system(bashCommand)
    return list_dest_gibbs

def preproc(list_dest_gibbs,flag_preproc):
    list_dest_preproc=list()
    for i in range (len(list_dest_gibbs)):
        s = "/"
        seq = list_dest_gibbs[i].split('/')
        temp = s.join(seq[0:6])+'/DTI-preproc/'
        temp_1=list_dest_gibbs[i].split('/')[-1].split('.')[0]+'_preproc.mif'
        destination_preproc = temp + temp_1
        list_dest_preproc.append(destination_preproc)
        if flag_preproc == True:
            bashCommand =("dwipreproc -rpe_header -eddy_options \" --slm=linear \" "+list_dest_gibbs[i]+' ' +destination_preproc)
            os.system(bashCommand)
    return list_dest_preproc


def mask(list_dest_preproc,flag_mask):
    list_dest_masked=list()
    for i in range (len(list_dest_preproc)):
        s = "/"
        seq = list_dest_preproc[i].split('/')
        temp = s.join(seq[0:6])+'/DTI-masked/'
        temp_1=list_dest_preproc[i].split('/')[-1].split('.')[0]+'_mask.mif'
        destination_masked = temp + temp_1
        temp_2 = list_dest_preproc[i].split('/')[-1].split('.')[0] + '_masked.mif'
        destination_masked_2 = temp + temp_2
        list_dest_masked.append(destination_masked_2)
        if flag_mask == True:
            bashCommand =("dwi2mask " +list_dest_preproc[i]+' '+destination_masked)
            os.system(bashCommand)
            bashCommand = ("mrcalc " + list_dest_preproc[i] +" "+destination_masked +" -mult "+destination_masked_2 )
            os.system(bashCommand)
    return list_dest_masked


def bias_correction(list_dest_masked,flag_bias):
    list_dest_bias=list()
    for i in range (len(list_dest_masked)):
        s = "/"
        seq = list_dest_masked[i].split('/')
        temp = s.join(seq[0:6])+'/DTI-bias/'
        temp_1=list_dest_masked[i].split('/')[-1].split('.')[0]+'_bias.mif'
        destination_masked = temp + temp_1
        list_dest_bias.append(destination_masked)
        if flag_bias == True:
            bashCommand =("dwibiascorrect -ants " +list_dest_masked[i]+' '+destination_masked)
            os.system(bashCommand)
            print("ok")
    return list_dest_bias



def remove_negative(list_dest_bias,flag_bias):
    list_dest_bias=list()
    for i in range (len(list_dest_masked)):
        s = "/"
        seq = list_dest_masked[i].split('/')
        temp = s.join(seq[0:6])+'/DTI-bias/'
        temp_1=list_dest_masked[i].split('/')[-1].split('.')[0]+'_bias.mif'
        destination_masked = temp + temp_1
        list_dest_bias.append(destination_masked)
        if flag_bias == True:
            bashCommand =("dwibiascorrect -ants " +list_dest_masked[i]+' '+destination_masked)
            os.system(bashCommand)
            print("ok")
    return list_dest_bias









def negative_remove():
    #img = nibabel.load('/home/visionlab/Desktop/work_dir/registration_folder/TRO_1yRz315_DTI_denoised_gibbs_preproc_masked_nifty.nii.gz')
    #data = img.get_data()
    #prova=(data-data.min())/(data.max()-data.min())
    #data = data.clip(min=0) #del the min value
    #clipped_img = nibabel.Nifti1Image(prova, img.affine, img.header)
    #nibabel.save(clipped_img,'/home/visionlab/Desktop/work_dir/registration_folder/TRO_1yRz315_DTI_denoised_gibbs_preproc_masked_nifty_modified_0.nii.gz')


    '''
    import nipype.interfaces.mrtrix as mrt
    mrconvert = mrt.MRConvert()
    mrconvert.inputs.in_file = '/home/visionlab/Desktop/work_dir/registration_folder/TRO_1yRz315_DTI_denoised_gibbs_preproc_masked_bias.mif'
    mrconvert.inputs.out_filename = '/home/visionlab/Desktop/work_dir/registration_folder/TRO_1yRz315_DTI_denoised_gibbs_preproc_masked_bias_0.nii'
    mrconvert.run()


    mrconvert '/home/visionlab/Desktop/work_dir/registration_folder/TRO_1yRz315_DTI_denoised_gibbs_preproc_masked_nifty_modified_non_negative.nii.gz'  '/home/visionlab/Desktop/work_dir/registration_folder/TRO_1yRz315_DTI_denoised_gibbs_preproc_masked_nifty_modified__non_negative.mif' -grad '/home/visionlab/Desktop/work_dir/registration_folder/TRO_1yRz315_DTI_denoised_gibbs_preproc_masked_0_0_0.txt' -force
    mrconvert '/home/visionlab/Desktop/work_dir/registration_folder/TRO_1yRz315_DTI_denoised_gibbs_preproc_masked.mif'  '/home/visionlab/Desktop/work_dir/registration_folder/TRO_1yRz315_DTI_denoised_gibbs_preproc_masked_prova.nii.gz' -export_grad_mrtrix '/home/visionlab/Desktop/work_dir/registration_folder/TRO_1yRz315_DTI_denoised_gibbs_preproc_masked_0_0_0.txt'
     /home/visionlab/mrtrix3-registration_multi_contrast/bin/population_template sh_b0000 sh_b0000.mif + sh_b1000 sh_b1000.mif -mask_dir mask -warp_dir warp -voxel_size 2

    '''

    return

