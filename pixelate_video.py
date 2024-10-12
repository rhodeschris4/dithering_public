from PIL import Image
import os
from dither_video import dither_image

def pixelate(image, block_size):
    # Resize the image to a smaller size
    small_image = image.resize(
        (image.width // block_size, image.height // block_size),
        resample=Image.BOX
    )
    # Resize the smaller image back to the original size
    pixelated_image = small_image.resize(image.size, Image.NEAREST)
    return pixelated_image

def pixelate_image():
        settings = {"file_name": "lib_frame", "block_size": 5} #for future # Define the block size for pixelation (higher block size results in more pixelation)

        for i in range(len(os.listdir("./frames")) - 1):
            image_path = "./frames/{}.jpg".format(settings["file_name"])
            image = Image.open(f"./frames/lib_frame{i}.jpg")

            # Apply pixelation effect
            pixelated_image = pixelate(image, settings["block_size"])

            # Save the pixelated image
            pixelated_image.save(f"./pixel_frames/lib_frame{i}.png")

        dither_image()


def main():
    # Open the image file
    # s = "knight.png"
    #img_name = input("Name of the file you would like to pixelate?: ")
    pixelate_image()



if __name__ == "__main__":
    main()


#village1_4_32_8
