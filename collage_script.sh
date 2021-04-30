echo "Running collage script..."
ffmpeg -i B.png -i A.png -filter_complex "[1]scale=iw/2:-1[b];[0:v][b] overlay" out1.png
ffmpeg -i out1.png -vf eq=brightness=100:saturation=200:contrast=-2000 -c:a copy out2.png

# first integer refers to an image index, seems like zero or one
# second number decreases the size of the second overlayed image as it increases and accepts floats
# third number seems to refer to index as well but seems to make no difference 
