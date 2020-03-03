""" 
File: pupil_prep.py
Contact: data@olicatschools.org

Description:
Clean and merge downloaded datasets into single file per key stage
"""

import os
import pandas as pd
import numpy as np


phonics_folder = 'Pho/'
phonics_columns = {'Last_Name' : 'text', 'First_Name' : 'text', 'UPN' : 'text', 'Gender' : 'text', 'DOB' : 'text', 'Disadvantaged' : 'text', 'EAL' : 'text', 'SEN' : 'text', 'Ethnicty' : 'text', 'Outcome' : 'text', 'Mark' : 'numeric'}

ks1_folder = 'Ks1/'
ks1_columns = {'Last_Name' : 'text', 'First_name' : 'text', 'UPN' : 'text', 'Gender' : 'text', 'DOB' : 'text', 'Disadvantaged' : 'text', 'EAL' : 'text', 'SEN' : 'text', 'Ethnicty' : 'text', 'KS1_Reading' : 'text', 'KS1_Writing' : 'text', 'KS1_Maths' : 'text', 'KS1_Science' : 'text'}

ks2_folder = 'Ks2/'
ks2_columns  = {'Last_Name' : 'text', 'First_Name' : 'text', 'UPN' : 'text', 'Gender' : 'text', 'DOB' : 'text', 'Disadvantaged' : 'text', 'EAL' : 'text', 'SEN' : 'text', 'Non_Mobile' : 'text', 'Ethnicity' : 'text', 'KS1_Reading_Level' : 'text', 'KS1_Reading_Band' : 'text', 'KS1_Writing_Level' : 'text', 'KS1_Writing_Band' : 'text', 'KS1_Maths_Level' : 'text', 'KS1_Maths_Band' : 'text', 'KS1_Points' : 'numeric', 'KS1_Band' : 'text', 'KS2_Reading_TA' : 'text', 'KS2_Reading_Scaled_Score' : 'numeric', 'KS2_Reading_Nominal_Scaled_Score' : 'numeric', 'KS2_Reading_Estimate' : 'numeric', 'KS2_Reading_Progress_Adjusted' : 'numeric', 'KS2_Reading_Progress_Unadjusted' : 'numeric', 'KS2_Reading_Expected' : 'text', 'KS2_Reading_High' : 'text', 'KS2_Maths_TA' : 'text', 'KS2_Maths_Scaled_Score' : 'numeric', 'KS2_Maths_Nominal_Scaled_Score' : 'numeric', 'KS2_Maths_Estimate' : 'numeric', 'KS2_Maths_Progress_Adjusted' : 'numeric', 'KS2_Maths_Progress_Unadjusted' : 'numeric', 'KS2_Maths_Expected' : 'text', 'KS2_Maths_High' : 'text', 'KS2_Writing_TA' : 'text', 'KS2_Writing_Nominal_Score' : 'numeric', 'KS2_Writing_Estimate' : 'numeric', 'KS2_Writing_Progress_Adjusted' : 'numeric', 'KS2_Writing_Progress_Unadjusted' : 'numeric', 'KS2_Writing_Expected' : 'text', 'KS2_Writing_High' : 'text', 'KS2_RWM_Expected' : 'text', 'KS2_RWM_High' : 'text', 'KS2_GPS_Scaled Score' : 'numeric', 'KS2_GPS_Expected' : 'text', 'KS2_GPS_High' : 'text', 'KS2_GPS_Spelling_Mark' : 'numeric', 'KS2_Science_TA' : 'text', 'KS2_Science_Expected' : 'text'}

ks4_folder = 'Ks4/'
ks4_columns = {'Last_Name' : 'text', 'First_Name' : 'text', 'UPN' : 'text', 'Gender' : 'text', 'DOB' : 'text', 'Disadvantaged' : 'text', 'EAL' : 'text', 'SEN' : 'text', 'Non_Mobile' : 'text', 'Ethnicity' : 'text', 'KS2_Reading_Score' : 'numeric', 'KS2_Reading_Band' : 'text', 'KS2_Maths_Score' : 'numeric', 'KS2_Maths_Band' : 'text', 'KS2_Overall_Score' : 'numeric', 'KS2_Overall_Band' : 'text', 'KS4_A8_Score' : 'numeric', 'KS4_A8_Estimate' : 'numeric', 'KS4_P8_Adjusted' : 'numeric', 'KS4_P8_Unadjusted' : 'numeric', 'KS4_5EM_Achieved' : 'text', 'KS4_Ebacc_Achieved' : 'text', 'KS4_English_Score' : 'numeric', 'KS4_English_Estimate' : 'numeric', 'KS4_English_Progress' : 'numeric', 'KS4_Maths_Score' : 'numeric', 'KS4_Maths_Estimate' : 'numeric', 'KS4_Maths_Progress' : 'numeric', 'KS4_Ebacc_Slot1' : 'numeric', 'KS4_Ebacc_Slot2' : 'numeric', 'KS4_Ebacc_Slot3' : 'numeric', 'KS4_Ebacc_Score' : 'numeric', 'KS4_Ebacc_Estimate' : 'numeric', 'KS4_Ebacc_Progress' : 'numeric', 'KS4_Open_Slot1' : 'numeric', 'KS4_Open_Slot2' : 'numeric', 'KS4_Open_Slot3' : 'numeric', 'KS4_Open_GCSE' : 'numeric', 'KS4_Open_NonGCSE' : 'numeric', 'KS4_Open_Score' : 'numeric', 'KS4_Open_Estimate' : 'numeric', 'KS4_Open_Progress' : 'numeric', 'KS4_Pillar_English_Entry' : 'text', 'KS4_Pillar_English_Achieved' : 'text', 'KS4_Pillar_Maths_Entry' : 'text', 'KS4_Pillar_Maths_Achieved' : 'text', 'KS4_Pillar_Science_Entry' : 'text', 'KS4_Pillar_Science_Achieved' : 'text', 'KS4_Pillar_Humanities_Entry' : 'text', 'KS4_Pillar_Humanities_Achieved' : 'text', 'KS4_Pillar_Language_Entry' : 'text', 'KS4_Pillar_Language_Achieved' : 'text'}


def prep_dataset(folder_name, col_headers):

  df_cleaned = pd.DataFrame()
  
  # Run through each file in a sub-folder of the current directory
  for file in os.listdir(folder_name):
    
    print(f'Working on {file}')

    # Append the folder suffix to the filename so python knows where to look
    file = folder_name + file

    # Load the current file into a dataframe, do not set column headers and load every value in as a string
    df_file = pd.read_excel(file, header = None).astype(str)
    
    # Set the column headers to be the keys from the col_headers dictionary (key : value)
    df_file = df_file.set_axis(col_headers.keys(), axis = 1, inplace = False)

    # If column is identified as numeric make it a number
    # If column is identified as text replace nan with blank 
    for col in df_file.columns:
      if col_headers[col] == 'numeric':
        df_file[col] = pd.to_numeric(df_file[col], errors = 'coerce')
      else:
        df_file[col] = df_file[col].replace('nan', '')
          
    
    # Remove the top three rows of the dataframe - clears the rubbish from the top of the export
    df_file = df_file[3:]

    # Add the year the results were achieved in
    df_file['Result_Year'] = file[-9:-5]

    # Add the urn of the school the student attended
    df_file['URN'] = file[4:10]

    # Extract the month of birth from the DOB column
    # Column needs to be handled as DateTime - remember it is currently a string
    df_file['BirthMonth'] = pd.DatetimeIndex(df_file['DOB']).month
    
    # Clean up some of the columns into codes
    df_file['Gender'] = df_file['Gender'].map({'Female' : 'F', 'Male' : 'M'})
    df_file['Disadvantaged'] = df_file['Disadvantaged'].map({'Yes' : 'Y', 'No' : 'N'})
    df_file['SEN'] = df_file['SEN'].map({'No SEN' : 'N', '' : 'N', 'SEN support' : 'K', 'SEN with statement or EHC plan' : 'E', 'SEN EHCP' : 'E'})
    df_file['EAL'] = np.select([df_file['EAL'] == 'English', df_file['EAL'] == ''], ['N', 'U'], 'Y')
    df_file['Minority_Ethnic'] = np.where(df_file['Ethnicity'] == 'White British', 'N', 'Y')

    # Append to master dataset
    df_cleaned = df_cleaned.append(df_file)

  return df_cleaned  


# Uncomment lines below to run prep

# phonics_dataset = prep_dataset(phonics_folder, phonics_columns)
# phonics_dataset.to_excel('phonics_data.xlsx', index = False)

# ks1_dataset = prep_dataset(ks1_folder, ks1_columns)
# ks1_dataset.to_excel('ks1_data.xlsx', index = False)

ks2_dataset = prep_dataset(ks2_folder, ks2_columns)
ks2_dataset.to_excel('ks2_data.xlsx', index = False)

# ks4_dataset = prep_dataset(ks4_folder, ks4_columns)
# ks4_dataset.to_excel('ks4_data.xlsx', index = False)
