from PIL import Image
import hitherdither
import random
import os
from frames_to_video import convert_to_video

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

#For extractig colors of the image not using the built in median
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

def dither_image():
    #Settings for dithering, could add more later
    settings = {"order": 32, "num_colors": 32}

    for i in range(len(os.listdir("./pixel_frames")) - 1):
        #neutral ish blue [5731396, 5376992, 12469561, 5755133, 9874880, 4990791, 110857, 9376745, 12390826, 5924979, 1916120, 11997295, 14624484, 6015479, 3242799, 15505862]
        #fave [16548578, 14939693, 10797052, 7701462, 1999212, 4139034, 7896417, 9418354, 15262771, 3661563, 13905847, 10920520, 13458561, 4418433, 12936496, 5802851]

        #For random colors
        #colors_list = generate_hex_colors(16)

        try:
            img = Image.open(f'./pixel_frames/lib_frame{i}.png')

            #List of colors i chose from testing random
            colors_list = get_image_palette_decimal(f'./pixel_frames/lib_frame{i}.png', settings["num_colors"])
            #colors_list = generate_hex_colors(16)
            palette = hitherdither.palette.Palette(colors_list)

            #palette = hitherdither.palette.Palette.create_by_median_cut(img)
            img_dithered = hitherdither.ordered.bayer.bayer_dithering(
               img, palette, [256/4, 256/4, 256/4], order=settings["order"])

            #img_dithered = hitherdither.diffusion.error_diffusion_dithering(img, palette, method="sierra2", order=2)

            img_dithered.save(f'./dither_frames/dither_lib{i}.png')
            print(f"Image {i} saved")

        except FileNotFoundError:
            print(f"Warning: File './pixel_frames/lib_frame{i}.png' not found. Skipping...")
            continue

    convert_to_video()


# if __name__ == "__main__":
#     main()

























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
