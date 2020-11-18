# SCAV
SCAV repository UPF
P1

############## Exercise 1 - RGB to YCbCr and YUV (rgb_yuv.py) #######################

First we open the image and resize it, get the data and plot the original one.
We could extract the rgb values of a concrete pixel (in my case, (120,120)).

Then we use the formula to convert to YCbCr in function of this RGB values. There are some different formulas in the internet, so I've been a little confused about the exact change of variables.

Then we could change to RGB again and prove that it is almost the same value, even if we have implemented the formulas to the conversion.

I found that to be able to perform a conversion to YUV I had to install the package cv2, that for an unknown reason I can't install, so I comment the code with the functions and commands I would use if I had a normal PC (puto mac de pijos)


############## Exercise 2 - Resize with ffmpeg (resize.py) #######################

We take the images from my local path (you may change it if you execute) and save it to a folder "processed" with the same name. This script takes the .jpg files and make a compression with 
-q:v x
where x its a number from 1 to 30 (when x is greater, worst quality -> less space

If there exist already some images in the processed folder, the code asks you to overwrite them.

We could observe than the size of the images with x=20 change to aproximately the half of the original size, and of course the quality is lower.

############## Exercise 3 - Lena B&W (lena_bw.py) #######################

We use the same commands to use ffmpeg in the python script as before.
The only difference is that in the command we will use 

-vf hue=s=0

so we de-saturate the image.
The other way to do this is killing the color channels with "format=grey" but I realized this command gave me a shitty result. 

############## Exercise 4 - Run-lenght encoding(run_lenght.py) #######################

The script counts the letters of a concrete string, joins the letter with his number and print the encoded string. I suppose for a series of bytes works the same way.
for example:
string = aabbcc
output = a2b2c2


############## Exercise 5 - DCT(dct.py) #######################

There are some functions that directly outputs a dct of a 2D image or matrix. Same thing for the IDCT (inverse). I couldn't prove this exercice because of the errors installing the packages to use this functions. 
The dct represents an image as a sum of sinusoids of varying magnitudes and frequencies. It is a lossy image compression algorithm JPEG, and the DCT is the heart of the whole process.


