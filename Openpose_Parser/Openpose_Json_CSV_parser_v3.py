import pandas as pd

def parse_nested_json(json_d):
    result = {}
    for key in json_d.keys():
        if not isinstance(json_d[key], dict):
            result[key] = json_d[key]
        else:
            result.update(parse_nested_json(json_d[key]))
    return result

json_data = pd.read_json("AR1_0001_keypoints.json")
json_list = [j[1][0] for j in json_data.iterrows()]
parsed_list = [parse_nested_json(j) for j in json_list]
result = pd.DataFrame(parsed_list)
result.to_csv("my_csv_file.csv", index=False)
