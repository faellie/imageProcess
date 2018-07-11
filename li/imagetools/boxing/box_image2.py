import Tkinter
from PIL import Image, ImageTk
from sys import argv
from matplotlib import pyplot as plt
import numpy as np
import tkMessageBox
import matplotlib.patches as patches
from matplotlib.widgets import Button
import os
import boxing.boxListManager
import boxing.boxList

x1=0.0
x2=0.0
y1=0.0
y2=0.0
boxes = []
boxpatches = []

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)




def onclick(event):
    global x1
    global y1
    if(event.xdata == None):
        return
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    x1=event.xdata
    y1=event.ydata

def onRelase(event):
    global x1
    global y1
    global x2
    global y2
    global boxes
    global boxpatches
    global rect
    # print('%s onRelase: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    #       ('double' if event.dblclick else 'single', event.button,
    #        event.x, event.y, event.xdata, event.ydata))
    if(event.xdata == None):
        return
    print('%s onRelase: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
                 ('double' if event.dblclick else 'single', event.button,
                  event.x, event.y, event.xdata, event.ydata))
    x2=event.xdata
    y2=event.ydata
    if(x1 != x2 ) :
        rect = patches.Rectangle((x1, y1),(x2-x1), (y2-y1),linewidth=2,edgecolor='r',facecolor='none')
        ax.add_patch(rect)
        boxes.append({'x1': x1, 'x2': x2,'y1': y1,'y2': y2})
        boxpatches.append(rect)
        print 'boxes : ', boxes
        plt.show()
    else :
        print 'single click'



def reset(event):
    global boxpatches
    global boxes
    print "reset called boxpatches " , len(boxpatches);
    boxes = []
    for arec in boxpatches:
        arec.remove()
    boxpatches = [];
    boxing.boxListManager.BoxListManager.clear()
    plt.show()

def save(event):
    global boxpatches
    global boxes
    print 'save ', boxes
    bm = boxing.boxListManager.BoxListManager();
    bm.add(boxes)
    boxes = []
    for arec in boxpatches:
        arec.remove()
    boxpatches = [];
    plt.close()

boxing.boxListManager.BoxListManager.clear()
PATH_TO_TEST_IMAGES_DIR = '/users/zihuangw/doc/personal/LI/Images'
TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, '{}.jpg'.format(i)) for i in range(1, 2) ]


for image_path in TEST_IMAGE_PATHS:
    boxing.boxListManager.BoxListManager.setCurrentImage(image_path)
    image = Image.open(image_path)
    image_np = load_image_into_numpy_array(image)
    fig = plt.figure()
    fig.set_size_inches(16, 12)
    ax = fig.subplots(1)

    press = fig.canvas.mpl_connect('button_press_event', onclick)
    release = fig.canvas.mpl_connect('button_release_event', onRelase)

    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    fig.text(0.05, 0.05, image_path, transform=ax.transAxes, fontsize=14,
              verticalalignment='top', bbox=props)
    # Display the image
    ax.imshow(image_np)


    button = Button(plt.axes([0.1, 0.9, 0.1, 0.04]), 'Reset', color='g', hovercolor='0.975')


    button.on_clicked(reset)


    savebutton = Button(plt.axes([0.1, 0.95, 0.1, 0.04]), 'Save', color='g', hovercolor='0.975')


    savebutton.on_clicked(save)

    plt.show()
bm = boxing.boxListManager.BoxListManager();
bm.toStr()
