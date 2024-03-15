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

    # Resize image
    img = cv2.resize(img, (640, 480))

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
    hsi_img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    return hsi_img

# Define the funcition to convert the image from HSI to RGB
def convert_hsi2rgb(img: cv2) -> cv2:
    """
    Covert the image from RGB to HSI
    
    Args: 
        img: The image to convert
        
    Returns: 
        The RGB image
    """
    rgb_img = cv2.cvtColor(img, cv2.COLOR_HLS2RGB)
    return rgb_img

"""
def convert_hsi2rgb(img: cv2) -> cv2:

    # Dividir la imagen en sus componentes HSI
    h, s, i = cv2.split(img)
    
    # Normalizar los valores de HSI al rango adecuado
    h = h / 180.0 * np.pi
    s = s / 255.0
    i = i * 255.0
    
    # Inicializar los componentes de color RGB
    r, g, b = np.zeros_like(h), np.zeros_like(h), np.zeros_like(h)
    
    # Caso 1: 0 <= H < 2*pi/3
    idx = (0 <= h) & (h < 2*np.pi/3)
    b[idx] = i[idx] * (1 - s[idx])
    r[idx] = i[idx] * (1 + s[idx] * np.cos(h[idx]) / np.cos(np.pi/3 - h[idx]))
    g[idx] = 3 * i[idx] - (r[idx] + b[idx])
    
    # Caso 2: 2*pi/3 <= H < 4*pi/3
    idx = (2*np.pi/3 <= h) & (h < 4*np.pi/3)
    r[idx] = i[idx] * (1 - s[idx])
    g[idx] = i[idx] * (1 + s[idx] * np.cos(h[idx] - 2*np.pi/3) / np.cos(np.pi - h[idx]))
    b[idx] = 3 * i[idx] - (r[idx] + g[idx])
    
    # Caso 3: 4*pi/3 <= H < 2*pi
    idx = (4*np.pi/3 <= h) & (h < 2*np.pi)
    g[idx] = i[idx] * (1 - s[idx])
    b[idx] = i[idx] * (1 + s[idx] * np.cos(h[idx] - 4*np.pi/3) / np.cos(np.pi/3 - h[idx]))
    r[idx] = 3 * i[idx] - (g[idx] + b[idx])
    
    # Apilar los componentes de color RGB en una imagen
    rgb_image = cv2.merge((b, g, r))
    
    # Convertir los valores RGB al rango [0, 255] y devolver la imagen
    return np.clip(rgb_image, 0, 255).astype(np.uint8)
"""

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

    hsi_image = cv2.imread("imageHSI-1.jpeg")
    hsi_image = cv2.resize(hsi_image, (640, 480))
    #Re convertir la imagen a RGB
    img3 = cv2.cvtColor(hsi_image, cv2.COLOR_HLS2RGB)

    cv2.imshow("new RGB Image", img3)

    # If you dont have an HSI image, use the line below, and use the image you just saved 
    #cv2.imwrite("imageHSI-2.jpeg",img2)
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
    elif args.conversion == "HSI2RGB":
        img_converted = convert_hsi2rgb(img)
        title = "HSI to RGB Image"
    else:
        print(f"ERROR! - Conversion type {args.conversion} is not supported")
    
    visualise_images(img, img_converted, "Input RGB Image", title)
    close_windows()


if __name__ == "__main__":
    pipeline()
    print('Program finished!\n')







