# Auto Photoshop Script

This script is designed to automate the process of adding one or more images to multiple frames in Adobe Photoshop and then save the resulting file as a JPEG image. It can be especially useful when you have a set of images and want to overlay them onto multiple frames.

This script is designed for use in an AWS environment and is intended to run on a dedicated server with minimal human interaction. It assumes that the server is fully vacant and does not require any manual keyboard input.
 

## Prerequisites

Before you can use this script, you'll need the following:

- [Adobe Photoshop](https://www.adobe.com/products/photoshop.html) installed on your computer.
- Find where temp files are stored on your computer (this is files that are opened up when images are added to frames)

## Usage

1. **Clone or Download the Repository**

   Clone this repository or download the script files to your local machine.

2. **Prepare Your Files**

   Place your source images (the images you want to overlay) and the frames (images to 
   which you want to add the source images) in a folder.

3. **Configure the Script**

   Open the `one_frame.py` or `multiple_frames.py` file in a text editor, and update the 
   following 
   variables:

   - `COUNTER_IMAGE`: How many images you want to loop through
   - `FRAME_NAME`: Name of the frame
   - `RESIZE_WIDTH` = what width frame needs image to be
   - `RESIZE_HEIGHT` = what height frame needs image to be
   - `path_store` = Where you add path to your images folder
   - `path_images` = Where images are found
   - `path_frame` = Path to frame
   - `path_temp` = Path to temp file


4. **Run the Script**

   Execute the script in a python environment:

   ```bash
   python3 one_file.py
