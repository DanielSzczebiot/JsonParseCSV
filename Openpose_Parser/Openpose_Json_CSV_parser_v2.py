import json
import csv
from pprint import pprint
# we are using pprint for making the output more readable.

with open('json/AR1_0001_keypoints.json') as f:
    data = json.load(f)
    #pprint(data)


with open('output.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(['pose_keypoints_2d', 'hand_left_keypoints_2d', 'hand_right_keypoints_2d'])

    for row in data:
        Pose = row['pose_keypoints_2d']
        Links = row['hand_left_keypoints_2d']
        Rechts = row['hand_right_keypoints_2d']

        row = [Pose, Links, Rechts]

        writer.writerow(row)
