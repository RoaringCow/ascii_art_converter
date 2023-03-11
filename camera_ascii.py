import cv2
import numpy as np

scale = 16
# set the frame width and height
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640 / scale * 2)# * 2 is there because chars height in ps are twice as big as the width of the chars
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480 / scale)

# create a list of brightness values for each ASCII character
ascii_chars = "   .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
brightness_levels = np.linspace(0, 255, len(ascii_chars) + 1)[1:]

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

def video_capture():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    data = np.array(gray)

    camera_to_ascii = convert_to_ascii(data, ascii_chars)

    ascii_lines = [''.join(row) for row in camera_to_ascii]
    ascii_in_a_string = '\n'.join(ascii_lines)
    print(ascii_in_a_string)


def camera_to_ascii():
    while True:
        video_capture()
    cap.release()