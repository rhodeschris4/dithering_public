from PIL import Image
import hitherdither
import random
import numpy as np
import os

# Generate random hex colors
def generate_hex_colors(num_colors):
    hex_colors = []
    for _ in range(num_colors):
        # Generate a random integer between 0 and 0xFFFFFF (16,777,215)
        color_int = random.randint(0, 0xFFFFFF)
        # Convert the integer to a hexadecimal string and prepend '0x'
        #hex_color = hex(color_int)
        hex_colors.append(0x000000 + color_int)
    return hex_colors

def get_image_palette_decimal(image_path, num_colors):
    """
    Extracts a palette of decimal color values from an image.

    Args:
        image_path: The path to the image file.
        num_colors: The desired number of colors in the palette.

    Returns:
        A list of integer color values (e.g., [9733009, 8632021, ...]).
    """
    img = Image.open(image_path).convert("RGB")
    img = img.quantize(colors=num_colors)

    palette = img.getpalette()

    decimal_colors = []
    for i in range(0, num_colors * 3, 3):
        r, g, b = palette[i:i + 3]
        decimal_color = (r << 16) + (g << 8) + b  # Convert RGB to decimal
        decimal_colors.append(decimal_color)

    return decimal_colors

def dither_image(pixelated_image_path):
    for i in range(1):
        settings = {"pixelated_file_path": pixelated_image_path, "num_colors": 32, "order": 32}

        # Generate 16 random hex colors
        # colors_list = generate_hex_colors(16)
        # print(colors_list)

        #palette = hitherdither.palette.Palette(colors_list) #custom palette

        image_path = settings["pixelated_file_path"] #./image_to_dither_DEBUG/village0_bs4.png
        base_name = os.path.basename(image_path) # get file name with .png (village0_bs4.png)
        pixelated_file_name = os.path.splitext(base_name)[0] # get file name w/out .png (village0_bs4)
        img = Image.open(image_path)

        #palette = hitherdither.palette.Palette.create_by_median_cut(img) #median cut palette

        # TEST DEBUG get x bit color palette
        colors_list = get_image_palette_decimal(image_path, settings["num_colors"]) #custom palette for images
        palette = hitherdither.palette.Palette(colors_list)

        #palette = hitherdither.palette.Palette.create_by_median_cut(img)
        img_dithered = hitherdither.ordered.bayer.bayer_dithering(
           img, palette, [256/4, 256/4, 256/4], order=settings["order"])


        #img_dithered = hitherdither.diffusion.error_diffusion_dithering(img, palette, method="sierra2", order=2)

        # save dithered image: filename_numcolors_order.png  ex.: knight_32_8.png
        image_path = "./current_dither_DEBUG/{0}_{1}_{2}.png".format(pixelated_file_name, settings["num_colors"], settings["order"])
        img_dithered.save(image_path)
        print(f"Image {i} saved")


def main():
    file_name="./image_to_dither_DEBUG/evil_nun_bs4.png"
    dither_image(file_name)


if __name__ == "__main__":
    main()

























# palette = hitherdither.palette.Palette(
#     [0x080000, 0x201A0B, 0x432817, 0x492910,
#      0x234309, 0x5D4F1E, 0x9C6B20, 0xA9220F,
#      0x2B347C, 0x2B7409, 0xD0CA40, 0xE8A077,
#      0x6A94AB, 0xD5C4B3, 0xFCE76E, 0xFCFAE2]
# )

# Brownish
# palette = hitherdither.palette.Palette(
#     [0x555358, 0x5F6062, 0x7B7263, 0xC6CA53,
#      0xC9DCB3]
# )
#66631F
#66551F
#1A1D33

#all brown
# palette = hitherdither.palette.Palette(
#     [0xF0D497, 0xF0BE97, 0xA797F0, 0x97B6F0,
#      0xBDB39D, 0xB0A49B, 0x9F9BB0, 0x8A806A,
#      0x705B4B, 0x524B70, 0x9BA2B0, 0x4B5870,
#      0x574B31, 0x332215, 0x1B1533, 0x152033]
# )
