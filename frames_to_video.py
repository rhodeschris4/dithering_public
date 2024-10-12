import cv2
import os

def convert_to_video():
    image_files = [f"./dither_frames/dither_lib{i:01d}.png" for i in range(len(os.listdir("./dither_frames")) - 1)]
    frame = cv2.imread(image_files[0])
    height, width, layers = frame.shape

    video = cv2.VideoWriter("./final_videos/lib.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 24, (width, height))

    for image in image_files:
        try:
            video.write(cv2.imread(image))
        except FileNotFoundError:
            print(f"Warning: File '{image}' not found. Skipping...")
            continue

    cv2.destroyAllWindows()
    video.release()

if __name__ == "__main__":
    convert_to_video()
