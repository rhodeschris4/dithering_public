from PIL import Image
import os
from dither import dither_image

def pixelate(image, block_size):
    # Resize the image to a smaller size
    small_image = image.resize(
        (image.width // block_size, image.height // block_size),
        resample=Image.BOX
    )
    # Resize the smaller image back to the original size
    pixelated_image = small_image.resize(image.size, Image.NEAREST)
    return pixelated_image

def pixelate_image(file_name):
    #img_name = input("Name of the file you would like to pixelate?: ") #for later, need to change dict when implemented
    settings = {"file_name": file_name, "block_size": 4} # make it easier to DEBUG, gonna add in video ones too

    # Open the image file
    image_path = "./image_to_pixelate_DEBUG/{}".format(settings["file_name"]) # can't do in one line with open
    image = Image.open(image_path)

    # Define the block size for pixelation (higher block size results in more pixelation)
    block_size = settings["block_size"]  # Example: increase to increase pixelation

    # Apply pixelation effect
    pixelated_image = pixelate(image, block_size)

    # Save the pixelated image
    pixelated_image_path = "./image_to_dither_DEBUG/{0}_bs{1}.png".format(settings["file_name"][:-4], block_size) #same here as mentioned above with save this time, bs stands for block_size
    pixelated_image.save(pixelated_image_path)

    dither_image(pixelated_image_path) #call dither with the pixelated image path

def main():
    pixelate_image("evil_nun.png")


if __name__ == "__main__":
    main()















#end
