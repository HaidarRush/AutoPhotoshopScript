################################################################## PHOTOSHOP AUTO #######################################################
"""This is a program to fully automate putting images in one frame on photoshop. I've tested this over 10,000 times and used it for my own
personal projects. If there are any questions feel free to message me on :

HaidarRush - Github"""

#############################################################################################################################################


from PIL import Image
from pathlib import Path
import win32com.client as win32
from photoshop import Session
import photoshop.api as ps
import pyautogui
import js2py

# how many images you have or what limit you want to set on finding the images
COUNTER_IMAGE = 80

# name of frame
FRAME_NAME = "05-Nook-16x20.psd"

# For use when resize is used
RESIZE_WIDTH = 729
RESIZE_HEIGHT = 1019

# Where you want to store new images folder
path_store = ""
# Where you add path to your images folder
path_images = ""

# Path to frame
path_frame = "C:\Users\Haidar\Desktop\Mockups that we like\Templates\PSD"

# need to find path to temp files on photoshop. this can be found when opening up a temp file in a frame and seeing where it is stored
path_temp = "C:\Users\Haidar\AppData\Local\Temp"

psd_file = r'C:\Users\Haidar\AppData\Local\Temp\Rectangle 1.psb'

# Opening photshop application
app = ps.Application()
# Opening up the first frame
app.load(rf'{path_frame}\{FRAME_NAME}')  # Opening the frame(template first)

# loops through images
for i in range(0, COUNTER_IMAGE):
    # located where the folder is with images
    current_folder = Path(f'{path_store}/photo_{i}')

    # Making a folder for the image
    current_folder.mkdir()

    # Open the image - change the name to whatever the image is called
    current_image = Image.open(rf'{path_images}\Poster_{i}.jpg')

    # Save the current image as a base within the new image folder
    current_image.save(f'{path_store}/Product{i}/Base_{i}.jpg')

    # Begining to interact with photoshop
    psApp = win32.Dispatch("Photoshop.Application")

    # open up the current image on photoshop
    app.load(rf'{path_images}\Poster_{i}.jpg')

    # Make sure this tab is the active tab
    doc = app.Application.ActiveDocument

    # resize the photo to fit the frame. This is one of the main bits that has to be edited
    # occuring to your image needs!
    doc.ResizeImage(RESIZE_WIDTH, RESIZE_HEIGHT, 300)

    # Select background layer
    layer_image = doc.ArtLayers['Background']

    # Copy layer (basically the image)
    layer_image.Copy()

    # Open up blank frame (when you double click the frame this opens up)
    app.load(rf'{path_temp}\Temp\Rectangle 1.psb')

    # making it the active document
    doc1 = app.Application.ActiveDocument

    # Pasting image
    doc1.Paste()

    # this is used to save the file, so that it will be shown on the main frame
    pyautogui.hotkey('ctrl', 's')

    # load up the frame again
    app.load(rf'{path_frame}\{FRAME_NAME}')  # Opening the frame(template first)

    # intilaise the image as jpeg
    options = ps.JPEGSaveOptions(quality=5)

    # Where would you like it saved
    jpg = current_folder

    # save the image as a jpeg
    doc.saveAs(jpg, options, True)

    # if you would like a alert saying it is saved
    app.doJavaScript(f'alert("save to jpg: {jpg}")')
    # image will have the same name as frame but with copy next to it. this is to change the name
    change_image = Image.open("05-Nook-16x20 copy.jpg")

    # this is where the image will be finally stored
    change_image.save(rf'{current_folder}\final.jpg')
