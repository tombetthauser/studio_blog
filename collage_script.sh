# echo $((1 + RANDOM % 1000))
# identify -format '%w %h' A.png

random_image_A="./collages/$(ls collages/ | sort -R | tail -n 1)"
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


output_file="collages/$(date +%s)-temp.png"

ffmpeg \
      -i "$random_image_A" \
      -i "$random_image_B" \
      -filter_complex \
       "[1:v] scale=$random_width_A1:$random_height_A1 [ovr1], 
       [1:v] scale=$random_width_B1:$random_height_B1 [ovrl2], 
       [0:v][ovr1] overlay=$random_width_A2:$random_height_A2 [temp1], 
       [temp1][ovrl2] overlay=$random_width_B2:$random_height_B2" \
       $output_file

random_contrast="$(($RANDOM%3-1)).$((0 + RANDOM % 50))"
random_saturation="$((0 + RANDOM % 3)).$((0 + RANDOM % 50))"
random_brightness="0.$((0 + RANDOM % 50))"

# random_contrast="$(($RANDOM%3-1)).$((0 + RANDOM % 100))"
# random_saturation="$((0 + RANDOM % 3)).$((0 + RANDOM % 100))"
# random_brightness="0.$((0 + RANDOM % 100))"

# ffmpeg -i $output_file -vf eq=contrast=$random_contrast -c:a copy "collages/$(date +%s)-c.png"


all_text=$(cat text.txt)

line_count=$(wc -l text.txt | awk '{ print $1 }')
rand_line_start=$((0 + RANDOM % $line_count))
# rand_line_end=$(expr $rand_line_start + $((0 + RANDOM % $line_count)))
rand_line_end=$(expr $rand_line_start)
text_lines=$(sed -n "$rand_line_start,$rand_line_end"p text.txt)


ffmpeg -i $output_file -vf \
  eq=brightness=$random_brightness:saturation=$random_saturation:contrast=$random_contrast,drawtext="fontfile=/path/to/font.ttf: \
    text='''$all_text''': \ 
    fontcolor=#$((0 + RANDOM % 10))$((0 + RANDOM % 10))$((0 + RANDOM % 10))$((0 + RANDOM % 10))$((0 + RANDOM % 10))$((0 + RANDOM % 10)): \ 
    fontsize=$(expr 5 + $((0 + RANDOM % 25))): \ 
    box=1: \ 
    boxcolor=black@0.5: \ 
    boxborderw=5: \ 
    x=(w-text_w)/2: \ 
    y=(h-text_h)/2" \
  -c:a copy "collages/$(date +%s).png"

rm $output_file

# ffmpeg -i input.mp4 -vf drawtext="fontfile=/path/to/font.ttf: \
# text='Stack Overflow': fontcolor=white: fontsize=24: box=1: boxcolor=black@0.5: \
# boxborderw=5: x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output.mp4

# first integer refers to an image index, seems like zero or one
# second number decreases the size of the second overlayed image as it increases and accepts floats
# third number seems to refer to index as well but seems to make no difference 
