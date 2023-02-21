import os
from PIL import Image

# Variables
img_dimension = 256

# Creates a list containing 5 lists, each of 8 items, all set to 0
rows, columns = 9, 9
Map = [[0 for x in range(rows)] for y in range(columns)]

def generate_random_map():
    #print_map()
    for i in range(len(Map)):
        for j in range(len(Map[i])):
                Map[i][j] = i  + (j * columns)


    #print_map()

def print_map():
    # Print the map in text
    lines = []
    for row in Map:
        lines.append(' '.join(str(x) for x in row))
    print('\n'.join(lines))

def create_image():
    path = r"./images/"
    dirs = os.listdir(path)

    # Open all images
    images = []
    # for item in dirs:
    #     print(item)
    #     im = Image.open(path + item)
    #     images.append(im)
    for j in range(columns):
        for i in range(rows):
            images.append(Image.new(mode="RGB", size=(img_dimension,img_dimension), color=(i*32, j*32, (i + j)*32)))



    # Create a new image as big as our Map
    new_im = Image.new('RGB', (img_dimension * rows, img_dimension * columns))

    # Create image
    x_offset = 0
    y_offset = 0
    for i in range(columns):
      x_offset = 0
      for j in range(rows):
          new_im.paste(images[Map[i][j]], (x_offset, y_offset))
          x_offset += images[Map[i][j]].size[0]
      y_offset += images[Map[i][j]].size[1]


    # Save new image
    new_im.save('test.png')

generate_random_map()
create_image()