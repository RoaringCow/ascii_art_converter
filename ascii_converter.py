import ascii_video
import camera_ascii
import image_to_ascii

def video_to_ascii(video):
    ascii_video.convert_video(video)

def ascii_camera():
    camera_ascii.camera_to_ascii()

def imageToAscii(image):
    image_to_ascii.image_to_ascii(image)

def script_control():
    print("What would you like to do?")
    print("type 1 for: video_to_ascii (saves to mp4)")
    print("type 2 for: ascii camera")
    print("type 3 for image to ascii(saves to txt)")
    action = int(input("type here:  "))
    if action == 1:
        video = input("type in the mp4 file including the extention:  ")
        video_to_ascii(video)
    elif action == 2:
        ascii_camera()
    elif action == 3:
        image = input("type in the image file including the extention:  ")
        imageToAscii(image)

if __name__ == "__main__":
    script_control()