import numpy as np
import pandas as pd
import os

PARENT_DIR = "C:/Users/joema/Desktop/Ghazi_AFM/033023/"
OUTPUT_FILE_PATH = "C:/Users/joema/Desktop/Ghazi_AFM/"
EXP_DATE = "033023"


def retrieve_modulus_column(path_to_xls):
    """
    Takes in the .xls file from the AFM instrument
    This file is not actually an .xls file so pd.read_excel will not work
    Instead parse the lines of the raw file and collect the data in the fourth column with a tab delimeter
    Return a pandas Series object containing the Young's Modulus column in kPa and the date of the experiment
    """

    with open(path_to_xls) as f:
        lines = f.readlines()

    young_modulus = []  # kPa
    for i in range(7, len(lines)):  # Data starts in line 7
        line = lines[i]
        line_split_list = line.split('\t')
        if line_split_list != ['\n']:  # Line between data and stats info
            modulus_value = line_split_list[3]  # Young's Modulus is in column 3
        else:
            modulus_value = np.NAN

        try:
            young_modulus.append(float(modulus_value) * 1000)
        except ValueError:
            young_modulus.append(np.NAN)  # This happens because there is an empty row before the stats begin

    young_modulus = pd.Series(young_modulus)
    date = lines[0]  # Report date in line 0
    date = date[date.find('(') + 1:date.find(')')].split(' ')[0]  # Find text between () and split off the timestamp

    return date, young_modulus


df = None
for root, dirs, files in os.walk(PARENT_DIR):
    for file in files:
        if file.endswith(".xls"):
            identity = file.split(".")[0]
            acquisition_date, modulus_series = retrieve_modulus_column(os.path.join(root, file))
            if df is None:
                df = pd.DataFrame(modulus_series, columns=[acquisition_date + "_" + identity])
            else:
                df = pd.concat([df, modulus_series.rename(acquisition_date + "_" + identity)], axis=1)

df.dropna(how='all', axis=1, inplace=True)
df.to_excel(OUTPUT_FILE_PATH + EXP_DATE + '.xlsx', index=False)
