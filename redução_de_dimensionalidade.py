import numpy as np
from PIL import Image

def gen_grayscale_image_array(path):
    image_array = np.array(Image.open(path))
    red, green, blue = image_array[:,:,0], image_array[:,:,1], image_array[:,:,2]
    grayscale_array = 0.2989 * red + 0.5870 * green + 0.1140 * blue
    return grayscale_array.astype(np.uint8)
    
def gen_binary_image_array(path):
    grayscale_image_array = gen_grayscale_image_array(path)
    binary_image = np.where(grayscale_image_array >= 128, 255, 0)
    return binary_image.astype(np.uint8)

def main():
    grayscale_image_array = gen_grayscale_image_array("lena.jpeg")
    binary_image_array = gen_binary_image_array("lena.jpeg")
    
    Image.fromarray(grayscale_image_array).save("grayscale-lena.jpeg")
    Image.fromarray(binary_image_array).save("binary-lena.jpeg")

main()

