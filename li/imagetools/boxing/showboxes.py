import matplotlib
import os
from PIL import Image
from matplotlib import pyplot as plt
import json
import numpy as np
from pprint import pprint
#import sys
#sys.path.append("../..")
import matplotlib.patches as patches

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)

with open('/opt/TF/tb/data/predict/out/data.json') as f:
    data = json.load(f)
    pprint(data)

for entry in data :
    print entry["image_path"]
    image = Image.open(os.path.join("./../../../", entry["image_path"]))
    image_np = load_image_into_numpy_array(image)
    fig,ax = plt.subplots(1)
    # Display the image
    ax.imshow(image_np)
    # Create a Rectangle patch
    for rect in entry["rects"] :
        rect = patches.Rectangle((rect["x1"],rect["y1"]),(rect["x2"] - rect["x1"]), (rect["y2"] - rect["y1"]),linewidth=2,edgecolor='r',facecolor='none')
        ax.add_patch(rect)
    plt.show()

    # for rect in entry["rects"] :
    #     print 'x = ',  rect["x1"] , '-' , rect["x2"]
    #     print 'y = ',  rect["y1"] , '-' , rect["y2"]



