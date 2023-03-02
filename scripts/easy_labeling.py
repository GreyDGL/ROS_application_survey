# This script is used to label the repository manually.

import os

# 0. read robot_resources.txt line by line

with open('robot_resources.txt', 'r') as f:
    resources = f.readlines()

# print(resources)

## create some general labels for reference:
labels = {"1": "simulator", "2": "algorithm", "3":"driver", "4": "visualization", "5": "model", "6": "system", 7: "other", 8: "none"}

# 1. Enumerate through the resources
resources_copy = resources.copy()
labeled_count = 0
try:
    for i, resource in enumerate(resources):
        if len(resource.split(" ")) != 2: # if the resource has been labeled
            labeled_count += 1
            continue
        else: # otherwise, the resource has been labeled
            print("You have labeled {} resources.".format(labeled_count))
            ## 1.1 print the resource
            print(resource)
            ## 1.2 ask user to label the resource
            print("Please choose the label for the resource:")
            print(labels)
            label = input("Please label the resource: ")
            label = label.lower()
            label = label.split(" ")

            final_label = ""
            for l in label:
                if l in labels.keys():
                    final_label += labels[l] + " "
            ## 1.3 write the label to the resource
            resources_copy[i] = resource.strip() + " " + final_label.strip() + "\n"
            ## 1.4 update the count
            labeled_count += 1
except Exception as e:
    print("Error", e)
finally:
    with open('robot_resources.txt', 'w') as f:
        f.writelines(resources_copy)
    print("You have labeled {} resources.".format(labeled_count))







