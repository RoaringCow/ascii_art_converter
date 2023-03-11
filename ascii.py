import numpy as np
import cv2

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


def convert_video(inputVideo):
    kontrol_listesi = []
    ascii_karakterleri = "   .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    for x in range(len(ascii_karakterleri)):
        kontrol_listesi.append(255 / len(ascii_karakterleri) * (x + 1))

    kalite_dusurme_oranı = int(input("Quality reduction rate?:  "))
    # Open the video file
    video = cv2.VideoCapture(inputVideo)

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    print("fps: {}".format(fps))
    # Get the total number of frames in the video
    totalframecount = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Total frame: {}".format(totalframecount))
    stacked_ascii_values = np.empty((totalframecount, int(height / kalite_dusurme_oranı), int(width / kalite_dusurme_oranı)), dtype='U1')

    print(stacked_ascii_values.shape)
    if stacked_ascii_values.shape[2] * 10 > 4000 or stacked_ascii_values.shape[1] * 10 > 4000:
        print("Too big. It might not work")
        print(stacked_ascii_values.shape[1] * 10)
        print(stacked_ascii_values.shape[2] * 10)
    # Iterate over each frame in the video and calculate its brightness values
    for x in range(totalframecount):
        success, frame = video.read(x)
        frame_resized = cv2.resize(frame, (int(width / kalite_dusurme_oranı), int(height / kalite_dusurme_oranı)))
        brightness_frame = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
        # Convert the brightness values to ASCII characters
        ascii_values = convert_to_ascii(brightness_frame, ascii_karakterleri)
        stacked_ascii_values[x] = ascii_values
        print("Loading %{}".format(x/totalframecount * 100))

    whole_frame = ""
    whole_frame_list = []

    print(stacked_ascii_values.shape[2])
    print(stacked_ascii_values.shape[1])
    # Define the dimensions of the output video
    width = stacked_ascii_values.shape[2] * 10
    height = stacked_ascii_values.shape[1] * 18

    print(width)
    print(height)
    # Define the output video codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height), isColor=False)

    # Define the font and font scale
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.35

    # Define the position of the first character
    x, y = 0, 0

    # Create a black background image
    background = np.zeros((height, width), dtype=np.uint8)

    # Iterate over each stack of ASCII characters and write them on the background image
    for i in range(0, stacked_ascii_values.shape[0], 1):
        stack = stacked_ascii_values[i]
        for j in range(0, stack.shape[0], 1):
            line = stack[j]
            for k in range(0, line.shape[0], 1):
                char = line[k]
                # Write the character on the background image
                cv2.putText(background, char, (x, y), font, font_scale, 255, 1, cv2.LINE_AA)
                # Move to the next character position
                x += 10
            # Move to the next line
            y += 18
            x = 0
        # Write the frame to the output video
        out.write(background)
        # Reset the position and clear the background image for the next frame
        x, y = 0, 0
        background.fill(0)
        print("Loading video %{}".format(i / stacked_ascii_values.shape[0] * 100))

    # Release the VideoWriter object and close the video file
    out.release
