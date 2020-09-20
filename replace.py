import re
import os

for nome in os.listdir('./arquivosCSV'):
    # open your csv and read as a text string
    with open('./arquivosCSV' + '/' + nome, 'r') as f:
        my_csv_text = f.read()

    find_str = ','
    replace_str = ';'

    # substitute
    new_csv_str = re.sub(find_str, replace_str, my_csv_text)

    # open new file and save
    new_csv_path = './' + nome  # or whatever path and name you want
    with open(new_csv_path, 'w') as f:
        f.write(new_csv_str)