from config_window import *
from iclass import Window


if __name__ == "__main__":
    wind = Window(width, heigth, resize, x, y, title, logo)
    wind.build()
    wind.set_image(image="resources/pig.jpg", size=(256, 256), position=(0, 500))
    wind.set_text(txt="HELLO", fg='black', position=(0, 20), font=("Arial", 20))
    wind.set_button(txt="click", background='red', position=(0, 50), font=("Arial Black", 12), event=lambda: print('click'))
    wind.run()
