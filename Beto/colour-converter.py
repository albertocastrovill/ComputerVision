"""
This program is a Python code that allows the user to specify the input image and conversion 
type using the command line.
The program uses the argparse library to parse the command line arguments.
The program uses the cv2 library to read and display the images.

Authors: Alberto Castro, Ana Bárbara Quintero and Hector Camacho
Organization: UDEM
Creation date: 27 February 2024
"""

# Import the required libraries
import cv2
import numpy as np
import argparse

# Define the function to parse the command line arguments
def parse_user_data():
    """
    Parse the command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_image', type=str, required=True, help="Specified input image url or location")
    parser.add_argument('--conversion', type=str, required=True, help="Specified conversion type")
    args = parser.parse_args()
    return args

# Define the function to load the image
def load_image(filename: str) -> cv2:
    """
    Load the image from the specified file

    Args:
        filename: The name of the file to load

    Returns:
        The image loaded from the file
    """
    img = cv2.imread(filename)
    if img is None:
        print(f"ERROR! - Image {filename} could not be read")
    return img

# Define the function to convert the image to grayscale
def convert_rgb2grey(img: cv2) -> cv2:
    """
    Convert the image to grayscale

    Args:
        img: The image to convert

    Returns:
        The grayscale image
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img

# Define the function to convert the image to HSV
def convert_rgb2hsv(img: cv2) -> cv2:
    """
    Convert the image to HSV

    Args:
        img: The image to convert

    Returns:
        The HSV image
    """
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return hsv_img

# Define the function to convert the image to HSI
def convert_rgb2hsi(img: cv2) -> cv2:
    """
    Convert the image to HSI

    Args:
        img: The image to convert

    Returns:
        The HSI image
    """
    hsi_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    return hsi_img

# Define the function to visualise both images
def visualise_images(img1: cv2, img2: cv2, title1: str, title2: str):
    """
    Visualise both images with their respective titles

    Args:
        img1: The first image to visualise
        img2: The second image to visualise
        title1: The title of the first image
        title2: The title of the second image
    """
    cv2.imshow(title1, img1)
    cv2.imshow(title2, img2)
    cv2.waitKey(0)

# Define function to close all windows
def close_windows():
    """
    Close all the OpenCV Windows
    """
    cv2.destroyAllWindows()

# Principal function
def pipeline():
    """
    Run the main pipeline function to convert the image to the specified type
    """
    args = parse_user_data()
    img = load_image(args.input_image)

    if args.conversion == "RGB2GREY":
        img_converted = convert_rgb2grey(img)
        title = "Grey Image"
    elif args.conversion == "RGB2HSV":
        img_converted = convert_rgb2hsv(img)
        title = "HSV Image"
    elif args.conversion == "RGB2HSI":
        img_converted = convert_rgb2hsi(img)
        title = "HSI Image"
    else:
        print(f"ERROR! - Conversion type {args.conversion} is not supported")
    
    visualise_images(img, img_converted, "Input RGB Image", title)
    close_windows()


if __name__ == "__main__":
    pipeline()
    print('Program finished!\n')



