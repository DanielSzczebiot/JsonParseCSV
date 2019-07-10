import rhinoscriptsyntax as rs
import json

#prompt the user for a file to import
filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
filename = rs.OpenFileName("Open JSON File", filter)

#Read JSON data into the datastore variable
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)

#Use the new datastore datastructure
print(datastore["pose_keypoints_2d"]["hand_left_keypoints_2d"]["hand_right_keypoints_2d"])
