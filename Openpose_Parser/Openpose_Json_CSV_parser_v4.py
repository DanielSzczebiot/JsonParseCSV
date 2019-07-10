import pandas as pd
import json

def json_csv(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return pd.DataFrame(data["people"]).to_csv(r'export_dataframe.csv', index = None, header=True)

print(json_csv('AR1_0001_keypoints.json'))




