from PIL import ImageGrab, Image, ImageSequence
import time
import imageio
import sys, os

save_folder = "C:\\Users\\Lenovo\\Desktop\\screen\\"
num_screens = 12 
gif_writer = imageio.get_writer(save_folder + "anim.gif", mode='I', duration = 0.7)

def screen(file_name):
    snapshot = ImageGrab.grab()
    save_path = save_folder + file_name
    snapshot.save(save_path)
    return save_path

with gif_writer:
    for screen_number in range(num_screens):
        file_name = "screen_" + str(screen_number + 1) + ".png"
        save_path = screen(file_name)
        gif_writer.append_data(imageio.imread(save_path))
        num_screens = num_screens - 1
        time.sleep(5)
    

