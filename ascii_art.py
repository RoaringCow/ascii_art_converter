from PIL import Image
import os
import cv2
import time

def ascii_cevir(input_image):
    # kopya varsa yok et
    #if os.path.exists(r"C:\Users\ersan\PycharmProjects\Ascii\downscaled.png"):
        #os.remove("downscaled.png")

    img = Image.open(input_image)

    # kaliteyi düşür
    img.thumbnail((256, 144))

    pixels = img.load()

    width = img.width

    kontrol_listesi= []
    ascii_karakterleri = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'."
    ascii_karakterleri = ascii_karakterleri[::-1]
    for x in range(len(ascii_karakterleri)):
        kontrol_listesi.append(255/len(ascii_karakterleri) * (x + 1))

    pixel_list = []
    brightness_list = []
    görüntü_listesi = []

    for y in range(img.height):
        for x in range(img.width):
            pixel = pixels[x, y] #rgb değerlerini al
            red, green, blue = pixel[0], pixel[1], pixel[2]
            brightness = 0.299 * red + 0.587 * green + 0.114 * blue #parlaklığı al
            brightness_list.append(brightness)

    for x in brightness_list: #her bir parlaklığı alıp bir karaktere yuvarla
        for i in kontrol_listesi:
            if i > x:
                if kontrol_listesi.index(i) < len(ascii_karakterleri):
                    if x + 3.75 >= i:
                        görüntü_listesi.append(ascii_karakterleri[kontrol_listesi.index(i)])
                    else:
                        görüntü_listesi.append(ascii_karakterleri[kontrol_listesi.index(i - 1)])
                    break
                else:
                    print("Sıçtın")

    listed_görüntü_list = []
    görüntü_listesi_lenght = len(görüntü_listesi)
    i = 0
    while görüntü_listesi_lenght > 0:
        transferring_string = ""
        for x in range(width):
            if i >= len(görüntü_listesi):
                break
            transferring_string += görüntü_listesi[i]
            i += 1
        listed_görüntü_list.append(transferring_string)
        görüntü_listesi_lenght -= width

    toplam_ve_cok_sisko_birlik.append(listed_görüntü_list)

    #img.save("downscaled.png")
    img.close()

toplam_ve_cok_sisko_birlik = []
# Load the video
video = cv2.VideoCapture("video.mp4")

start_time = cv2.getTickCount()

# Check if the video was opened successfully
if not video.isOpened():
    print("Error opening the video")
    exit()

# Get the total number of frames in the video
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

print("Total number of frames in the video:", total_frames)

for x in range(total_frames):
    # Set the position of the video to the specified frame
    video.set(cv2.CAP_PROP_POS_FRAMES, x)

    # Read the specified frame
    ret, frame = video.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error reading the frame")
        break

    # Do your processing here
    percentage = int(x / total_frames * 100)
    print("loading %{}".format(percentage))
    # Save the processed image as a PNG file
    cv2.imwrite("frame_{}.png".format(x), frame)
    #os.remove("frame_{}.png".format(x))
    ascii_cevir("frame_{}.png".format(x))

# Release the video
video.release()

for x in toplam_ve_cok_sisko_birlik:
    os.system("cls")
    for i in x:
        print(i)
    time.sleep(100 /3000)