# echo $((1 + RANDOM % 1000))
# identify -format '%w %h' A.png

random_image_A="./images/$(ls images/ | sort -R | tail -n 1)"
random_image_B="./images/$(ls images/ | sort -R | tail -n 1)"

width_A=$(identify -format '%w' "$random_image_A")
height_A=$(identify -format '%h' "$random_image_A")
width_B=$(identify -format '%w' "$random_image_B")
height_B=$(identify -format '%h' "$random_image_B")

random_width_A1=$((1 + RANDOM % $width_A))
random_height_A1=$((1 + RANDOM % $height_A))
random_width_B1=$((1 + RANDOM % $width_B))
random_height_B1=$((1 + RANDOM % $height_B))

random_width_A2=$((1 + RANDOM % $width_A))
random_height_A2=$((1 + RANDOM % $height_A))
random_width_B2=$((1 + RANDOM % $width_B))
random_height_B2=$((1 + RANDOM % $height_B))

# version="0002"
# expr $height + 0
# expr $version + 1

# ffmpeg -i B.png -i A.png -filter_complex "[1]scale=iw/2:-1[b];[0:v][b] overlay" out1.png


output_file="collages/$(date +%s).png"

ffmpeg \
      -i "$random_image_A" \
      -i "$random_image_B" \
      -filter_complex \
       "[1:v] scale=$random_width_A1:$random_height_A1 [ovr1], 
       [1:v] scale=$random_width_B1:$random_height_B1 [ovrl2], 
       [0:v][ovr1] overlay=$random_width_A2:$random_height_A2 [temp1], 
       [temp1][ovrl2] overlay=$random_width_B2:$random_height_B2" \
       $output_file

random_brightness=$((-2 + RANDOM % 2))
random_saturation=$((-2 + RANDOM % 2))
random_contrast=$((-2 + RANDOM % 2))

random_decimal_A="$(($RANDOM%3-1)).$((0 + RANDOM % 25))"

ffmpeg -i $output_file -vf eq=contrast=$random_decimal_A -c:a copy "collages/$(date +%s)-c.png"
# ffmpeg -i $output_file -vf eq=brightness=$random_decimal:saturation=$random_decimal:contrast=$random_decimal_A -c:a copy "collages/$(date +%s)-c.png"

# first integer refers to an image index, seems like zero or one
# second number decreases the size of the second overlayed image as it increases and accepts floats
# third number seems to refer to index as well but seems to make no difference 
