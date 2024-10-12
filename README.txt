Welcome to this dithering application I created!!

PREFACE: This readme was made for friends who do not know anything coding related haha
Also, i am creating a web application for this using nextjs and mongoDB, and instead of using libraries like PIL, i use numpy to convert the images into numpy arrays and do the logic on those, it is definetly faster but I was using PIL because I wanted to see the images at each step for debugging reasons.

So there may be some issues along the way and I can help you with those (I am creating a fullstack app that will work on a website).
Steps:
1. Download the zip file and save somehwere where it makes sense. Like Documents/Code or something. Basically save it in a folder called code in your documents. Just a house keeping thing but it will make your life a lot easier if you code in the future (could even do Documents/Code/Python)
2. Ok so the main file to run the program is extract_frames.py. There is a line of code: 'video_name_DEBUG = "./videos/red_eye_video_c.mp4" # or any other extension like .avi etc', replace the "red_eye_video_c.mp4" with the name of your video file. IT MUST BE IN MP4. You can definetly change this but this is the case for now.
    If you have a non mp4 file, you just rename the video file you want and add .mp4, and it should bring up a prompt asking if you want to change it and you select YES (on mac).
3. So there are some settings you can play around with. I will first explain the workflow of this application:
    a. High Level Workflow: Upload a video file, outputs a dithered version of that video you uploaded
    b. More Low Level: Upload a video, extract all of the frames from the video; run a pixelation algorithm on each frame; feed those frames into the dithering algorithm to dither each frame; recieve each frame and put back into a video (.mp4)

Settings
So you will need a code editor to change the settings, I reccomend Zed (on mac). I can walk you through how to use it.
But, there are some settings you should be aware of.
    a. pixel_video.py: to change the amount of pixelation, change the block_size variable on line 16. the higher the more resolution, the lesser the less the resolution. i think that's how it works, try it out for yourself lol.
    b.dither_video.py: On line 45, there is a dictionary object called settings. settings = {"order": 32, "num_colors": 32}, the order i think is the resolution of gridding for the dithering algo? idk you can find out. but the colors setting is the amount of colors that it will take when running the algo. I HIIGHLY SUGGEST only using multiples of 8. You can try with others I really have not lmao... Actually I think I tried with 24 and it worked, you do you.

BONUS
If you want to get wild with how the colors are in the image, there is some code code you will have to uncomment.

DEBUG (for images and debugging, no video)
pixelate_one_image.py / dither.py ; So I created some functions/files you can debug with. I will start with pixelate_one_image.py
    a.You MUST save the image in image_topixelate_DEBUG, and then change line
    def main():
        pixelate_image("evil_nun.png"), it is line 36, change the "evil_nun.png" to whatever file you have saved. I would recommend it be a png ; run 'python pixelate_one_image' ; and if you changed the file directory to the image you want, it should work
    b. ok the pixelated image is saved to /image_to_dither_DEBUG directory. Now run dither.py, but change line 77 for the exact file name. def  main():
        file_name="./image_to_dither_DEBUG/evil_nun_bs4.png", example woule be file_name="./image_to_dither_DEBUG/poop_bs4.png", the bs4 will change, that is just a file structure naming convention i came up with for the pxiel block you choose in the pixelation algorithm
    c. There is also a line of code within the dithering algorithm that allows you to create some experimental coloring. Right now it takes a median color sample of the entier image. However, if you uncomment these lines in dither.py:
        # Generate 16 random hex colors
        # colors_list = generate_hex_colors(16)
        # print(colors_list)

        #palette = hitherdither.palette.Palette(colors_list) #custom palette
    and comment this line out 'colors_list = get_image_palette_decimal(image_path, settings["num_colors"]) #custom palette for images', you should get the experimental part working. Basically instead of taking a median cut of the colors (in this case it would be 32 colors for how the settings are by default, it will create a random color palette).


MUST READ DEBUG
So for the debug, if you upload an image and run the commands above it should work.I definetly left something out so let me know!!
