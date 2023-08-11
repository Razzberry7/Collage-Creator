import tkinter as tk
import os
import shutil
from enum import Enum
from PIL import Image

# path_dir = input("What is the dir of the path of images? (ex: D:\Gamedev Projects and More\Other Projects\Dad Projects\Penthouse Shirt\) \n>")
# img_dimension = int(input("What are the dimensions of the images? (ex: 256) \n>"))
# grid_dimension = int(input("What are the dimensions of the grid? (ex: 18 x 18, is just 18) \n>"))
# grid_mode = int(input("What kind of grid do you want to generate? (0 = tiles, 1 = staggered tiles, 2 = dark/white boxes), 3 = white/dark boxes) \n>"))
# grid_name = input("What do you want to call the GRID? (ex: Beatles_Grid.png) \n>")

# Enum for mode
class Mode(Enum):
    TILED = 0
    TILED_STAGGERED = 1
    DARK_WHITE = 2
    WHITE_DARK = 3

path_dir = ""
img_dimension_w, img_dimension_h = ["100", "100"]
grid_dimension_w, grid_dimension_h = ["1", "1"]
grid_mode = "TILED"
settings_bools = [False, False, False]
grid_name = "/Results/default.png"
img_dimensions = [100, 100]
rows, columns = 1, 1
Map = [[0]]



def get_inputs():
    global path_dir, img_dimension_w, img_dimension_h, grid_dimension_w, grid_dimension_h, grid_mode, settings_bools,\
        grid_name

    path_dir = path_entry.get()
    # print(path_dir)

    img_dimension_w = int(img_dim_entry_w.get())
    img_dimension_h = int(img_dim_entry_h.get())
    # print(str(img_dimension_w) + " " + str(img_dimension_h))

    grid_dimension_w = int(grid_dim_entry_w.get())
    grid_dimension_h = int(grid_dim_entry_h.get())
    # print(str(grid_dimension_w) + " " + str(grid_dimension_h))

    grid_mode = grid_mode_var.get()
    # print(grid_mode)

    settings_bools = [settings_allow_dark_var.get(), settings_allow_light_var.get(), settings_allow_other_var.get()]
    # print(settings_bools)

    grid_name = "/Results/" + filename_entry.get() + ".png"
    # print(grid_name)

def create_variables():
    global img_dimensions, rows, columns, Map

    # img_dimensions = [300, 415]
    img_dimensions = [int(img_dimension_w), int(img_dimension_h)]
    rows, columns = int(grid_dimension_w), int(grid_dimension_h)

    # Creates a list containing 5 lists, each of 8 items, all set to 0
    Map = [[0 for x in range(rows)] for y in range(columns)]
    print(Map)

root = tk.Tk()
root.geometry("1000x400") # Set the width and height of the window

title = tk.Label(root, text="Grid Creator, by: Brandon McHenry", font=("Helvetica", 20, "bold"))
title.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

# <editor-fold desc="Path GUI">
path_frame = tk.Frame(root)

path_label = tk.Label(path_frame, text="Path directory: ", font=("Helvetica", 16, "bold"))
path_label.pack(side=tk.LEFT)

path_entry = tk.Entry(path_frame, text="Path directory: ", width=100)
path_entry.pack(side=tk.LEFT, padx=10)

path_frame.place(relx=0.5, rely=0.2, anchor=tk.CENTER) # Center the frame
# </editor-fold>

# <editor-fold desc="Img Dimensions GUI">
img_dim_frame = tk.Frame(root)

img_dim_label = tk.Label(img_dim_frame, text="Image Dimensions (Width x Height): ", font=("Helvetica", 16, "bold"))
img_dim_label.pack(side=tk.LEFT)

img_dim_entry_w = tk.Entry(img_dim_frame, width=20)
img_dim_entry_w.pack(side=tk.LEFT, padx=10)

img_dim_label_x = tk.Label(img_dim_frame, text="x")
img_dim_label_x.pack(side=tk.LEFT, padx=10)

img_dim_entry_h = tk.Entry(img_dim_frame, width=20)
img_dim_entry_h.pack(side=tk.LEFT, padx=10)

img_dim_frame.place(relx=0.5, rely=0.3, anchor=tk.CENTER) # Center the frame
# </editor-fold>

# <editor-fold desc="Grid Dimension GUI">
grid_dim_frame = tk.Frame(root)

grid_dim_label = tk.Label(grid_dim_frame, text="Grid Dimensions (Width x Height): ", font=("Helvetica", 16, "bold"))
grid_dim_label.pack(side=tk.LEFT)

grid_dim_entry_w = tk.Entry(grid_dim_frame, width=20)
grid_dim_entry_w.pack(side=tk.LEFT, padx=10)

grid_dim_label_x = tk.Label(grid_dim_frame, text="x")
grid_dim_label_x.pack(side=tk.LEFT, padx=10)

grid_dim_entry_h = tk.Entry(grid_dim_frame, width=20)
grid_dim_entry_h.pack(side=tk.LEFT, padx=10)

grid_dim_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER) # Center the frame
# </editor-fold>

# <editor-fold desc="Grid Mode GUI">
grid_mode_frame = tk.Frame(root)

grid_mode_label = tk.Label(grid_mode_frame, text="Grid mode: ", font=("Helvetica", 16, "bold"))
grid_mode_label.pack(side=tk.LEFT)

grid_mode_var = tk.StringVar(value=Mode.TILED.name)
# grid_mode_options = ["Tiles", "Staggered Tiles", "Dark/white Boxes", "White/dark Boxes"]
for mode in Mode:
    grid_mode_rb = tk.Radiobutton(grid_mode_frame, text=mode.name, variable=grid_mode_var, value=mode.name)
    grid_mode_rb.pack(side=tk.LEFT, padx=10)

grid_mode_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Center the frame
# </editor-fold>

# <editor-fold desc="Extra Settings GUI">
settings_frame = tk.Frame(root)

settings_label = tk.Label(settings_frame, text="Settings: ", font=("Helvetica", 16, "bold"))
settings_label.pack(side=tk.LEFT)

settings_allow_dark_var = tk.BooleanVar()
settings_allow_dark_cb = tk.Checkbutton(settings_frame, text="Allow dark photos?", variable=settings_allow_dark_var)
settings_allow_dark_cb.pack(side=tk.LEFT)

settings_allow_light_var = tk.BooleanVar()
settings_allow_light_cb = tk.Checkbutton(settings_frame, text="Allow light photos?", variable=settings_allow_light_var)
settings_allow_light_cb.pack(side=tk.LEFT)

settings_allow_other_var = tk.BooleanVar()
settings_allow_other_cb = tk.Checkbutton(settings_frame, text="Allow other photos?", variable=settings_allow_other_var)
settings_allow_other_cb.pack(side=tk.LEFT)

settings_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER) # Center the frame
# </editor-fold>

# <editor-fold desc="Grid Filename GUI">
filename_frame = tk.Frame(root)

filename_label = tk.Label(filename_frame, text="Grid filename: ", font=("Helvetica", 16, "bold"))
filename_label.pack(side=tk.LEFT)

filename_entry = tk.Entry(filename_frame, width=25)
filename_entry.pack(side=tk.LEFT, padx=10)

filename_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER) # Center the frame
# </editor-fold>

button = tk.Button(root, text="< Generate Grid >",
                   command=lambda: [get_inputs(), create_variables(), generate_random_map(), create_image()])
button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


# Creates a new dir to store hashed version of the original images.
# This is so that the grid can randomize the placement of images.
def hash_images_for_randomization():
    # path = r"D:\Gamedev Projects and More\Other Projects\Dad Projects\Custom 70s Shirt"

    # Get the path of the parent folder
    path = path_dir

    # Make a TOTAL folder if one doesn't exist, if it does exist, delete it and remake it
    dir_path = path + "\\TOTAL\\"
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
        os.mkdir(dir_path)
    else:
        os.mkdir(dir_path)

    # Open the folder at this path (contains the actual images)
    new_path = path + "\\Other Images"
    top_dir = os.listdir(new_path)

    # Open all images in the dir and save them as a hash in the TOTAL dir (for random grid image creation)
    for folders in top_dir:
        for item in os.listdir(new_path + "\\" + folders + "\\"):
            print(folders + " and " + item)
            im = Image.open(new_path + "\\" + folders + "\\" + item).convert('RGB')
            im.save(dir_path + str(hash(folders + item)) + ".jpg")

# Actually create the grid, based on the grid mode
def create_image():
    global path_dir, grid_mode

    # path = r"D:\Gamedev Projects and More\Other Projects\Dad Projects\Custom 70s Shirt\TOTAL"
    # Path where images are
    path = path_dir
    print(path_dir)
    top_dir = os.listdir(path)
    print(top_dir)

    print(grid_mode)
    print(Mode.TILED_STAGGERED)
    print(Mode["TILED_STAGGERED"] == Mode.TILED_STAGGERED)

    # Switch for different types of grids
    match Mode[grid_mode]:
        # <editor-fold desc="Create a grid in normal tiled mode">
        case Mode.TILED:
            print("Creating a grid in normal tiled mode... ")

            # Open all images
            images = []
            for files in top_dir:
                im = Image.open(path + "\\" + files)
                im = im.resize((img_dimensions[0], img_dimensions[1]))
                images.append(im)

            # Create a new image as big as our Map
            new_im = Image.new('RGB',
                               (img_dimensions[0] * rows, (img_dimensions[1] * columns) - img_dimensions[1] // 2))

            print(Map)

            # Create image
            x_offset = 0
            y_offset = 0
            for i in range(columns):
                x_offset = 0
                for j in range(rows):
                    print(images[Map[i][j]])
                    if is_odd(j):
                        y_offset = y_offset - images[Map[i][j]].size[1] // 2
                    else:
                        y_offset = y_offset + images[Map[i][j]].size[1] // 2
                    new_im.paste(images[Map[i][j]], (x_offset, (y_offset)))
                    x_offset += images[Map[i][j]].size[0]
                y_offset += images[Map[i][j]].size[1]

            # Save new image
            new_im.save(grid_name)
        # </editor-fold>

        # <editor-fold desc="Create a grid in staggered tiled mode">
        case Mode.TILED_STAGGERED:
            print("Creating a grid in staggered tiled mode...")

            # Open all images
            images = []
            for folders in top_dir:

                if settings_bools[0]:
                    folder_path = path + "\\" + folders + "\\Dark"
                    # print(folder_path)
                    if os.path.exists(folder_path):
                        for image in os.listdir(folder_path):
                            # print(folder_path + "\\" + image)
                            im = Image.open(folder_path + "\\" + image)
                            im = im.resize((img_dimensions[0], img_dimensions[1]))
                            # print(im)
                            images.append(im)

                if settings_bools[1]:
                    folder_path = path + "\\" + folders + "\\Light"
                    # print(folder_path)
                    if os.path.exists(folder_path):
                        for image in os.listdir(folder_path):
                            # print(folder_path + "\\" + image)
                            im = Image.open(folder_path + "\\" + image)
                            im = im.resize((img_dimensions[0], img_dimensions[1]))
                            # print(im)
                            images.append(im)

                if settings_bools[2]:
                    folder_path = path + "\\" + folders + "\\Other"
                    # print(folder_path)
                    if os.path.exists(folder_path):
                        for image in os.listdir(folder_path):
                            # print(folder_path + "\\" + image)
                            im = Image.open(folder_path + "\\" + image)
                            im = im.resize((img_dimensions[0], img_dimensions[1]))
                            # print(im)
                            images.append(im)

                if not settings_bools[0] and not settings_bools[1] and not settings_bools[2]:
                    folder_path = path + "\\" + folders
                    # print(folder_path)
                    if os.path.exists(folder_path):
                        for image in os.listdir(folder_path):
                            # print(folder_path + "\\" + image)
                            im = Image.open(folder_path + "\\" + image)
                            im = im.resize((img_dimensions[0], img_dimensions[1]))
                            # print(im)
                            images.append(im)


            # print(images)

            # Create a new image as big as our Map
            new_im = Image.new('RGB',
                               (img_dimensions[0] * rows, (img_dimensions[1] * columns) - img_dimensions[1] // 2))

            # Create image
            x_offset = 0
            y_offset = -200
            for i in range(columns):
                x_offset = 0
                for j in range(rows):
                    if is_odd(j):
                        y_offset = y_offset - images[Map[i][j]].size[1] // 2
                    else:
                        y_offset = y_offset + images[Map[i][j]].size[1] // 2
                    print(Map[i][j])
                    print(images[Map[i][j]])
                    new_im.paste(images[Map[i][j]], (x_offset, (y_offset)))
                    x_offset += images[Map[i][j]].size[0]
                y_offset += images[Map[i][j]].size[1]

            # Save new image
            new_im.save(grid_name)
        # </editor-fold>

        # <editor-fold desc="Create a grid in squares mode (dark inside, white border)">
        case Mode.DARK_WHITE:
            print("Creating a grid in squares mode (dark inside, white border)...")

            # Open all images
            images = []
            for files in top_dir:
                im = Image.open(path + "\\" + files)
                im = im.resize((img_dimensions[0], img_dimensions[1]))
                images.append(im)

            # Create a new image as big as our Map
            new_im = Image.new('RGB',
                               (img_dimensions[0] * rows, (img_dimensions[1] * columns) - img_dimensions[1] // 2))

            # Create image
            x_offset = 0
            y_offset = 0
            for i in range(columns):
                x_offset = 0
                for j in range(rows):
                    if is_odd(j):
                        y_offset = y_offset - images[Map[i][j]].size[1] // 2
                    else:
                        y_offset = y_offset + images[Map[i][j]].size[1] // 2
                    new_im.paste(images[Map[i][j]], (x_offset, (y_offset)))
                    x_offset += images[Map[i][j]].size[0]
                y_offset += images[Map[i][j]].size[1]

            # Save new image
            new_im.save(grid_name)
        # </editor-fold>

        # <editor-fold desc="Create a grid in squares mode (white inside, dark border">
        case Mode.WHITE_DARK:
            print("Creating a grid in squares mode (white inside, dark border)...")
        # </editor-fold>

        case _:
            print("No grid mode entered... EXITING...")
            return



##### Utility Methods #####

# If you need individual photos from a perfectly square grid of square images
def split_up_grid(filename, cols, rows):
    # path = r"D:\Gamedev Projects and More\Other Projects\Dad Projects\Custom 70s Shirt\\"
    path = path_dir
    dir_path = path + filename[:-4]
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
        os.mkdir(dir_path)
    else:
        os.mkdir(dir_path)

    grid = Image.open(path + filename)
    w, h = grid.size
    unitw = w // cols
    unith = h // rows
    for n in range(rows):
        for m in range(cols):
            newImage = grid.crop((unitw * m, unith * n, unitw * (m + 1), unith * (n + 1)))
            newImage.save(path + filename[:-4] + "\\" + str(hash(str((n * cols) + m + 1))) + ".png")

# Generating a random map
def generate_random_map():
    #print_map()
    for i in range(len(Map)):
        for j in range(len(Map[i])):
                Map[i][j] = i  + (j * columns)
    #print_map()

# Printing map
def print_map():
    # Print the map in text
    lines = []
    for row in Map:
        lines.append(' '.join(str(x) for x in row))
    print('\n'.join(lines))

# Determine if given number is odd
def is_odd(number):
    return True if number % 2 == 1 else False


##### End of Utility Methods #####


##### Running Program #####

# hash_images_for_randomization()

# # Generate a random map and print it in the console
# generate_random_map()
#
# # Create a grid image
# create_image()

# Split up a square grid image that is 17 images by 12 images
# split_up_grid("IMG_0089.jpg", 17, 12)

root.mainloop()

##### End of Running Program #####