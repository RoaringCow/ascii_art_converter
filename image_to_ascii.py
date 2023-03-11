from PIL import Image
import numpy as np


def convert_to_ascii(arr, ascii_chars):
    # Create an empty 2D array to store the ASCII characters
    ascii_frame = np.empty(arr.shape[:2], dtype='str')

    # Iterate over each pixel in the array and map its brightness to an ASCII character
    char_indices = np.floor_divide(arr, 255 / len(ascii_chars)).astype(int)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            char_index = char_indices[i, j]
            if char_index < len(ascii_chars):
                ascii_frame[i, j] = ascii_chars[char_index]

    return ascii_frame


def save_txt(my_array):
    with open('ascii.txt', 'w') as f:
        for row in my_array:
            row_string = ''.join([a for a in row])
            f.write(row_string + '\n')


def image_to_ascii(img):
    image = Image.open(img)
    rgb_im = image.convert('L')
    brightness_array = np.array(rgb_im)
    ascii_chars = "               .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"#12
    save_txt(convert_to_ascii(brightness_array, ascii_chars))