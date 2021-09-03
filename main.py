from config_window import *
from PIL import ImageTk, Image

from tkinter import Tk, Label, Button


class Window:
    def __init__(self, width, heigth, tranform, xpos, ypos, title, logo):
        self.width = width
        self.heigth = heigth
        self.tranform = tranform
        self.xpos = xpos
        self.ypos = ypos
        self.title = title
        self.logo = logo
        self.root = Tk()
    
    def build(self):
        self.root.geometry(f"{self.width}x{self.heigth}"
                           f"+{self.xpos}+{self.ypos}")
        self.root.resizable(*self.tranform)
        self.root.iconbitmap(default=self.logo)
        self.root.title(self.title)
    
    def run(self):
        self.root.mainloop()
    
    def set_text(self, txt, fg, position, font_param, bg=None):
        Label(self.root, text=txt, background=bg, foreground=fg, font=font_param).place(x=position[0],
                                                                                        y=position[1])
    
    def set_image(self, image, size, position):
        global tkimage
        img = Image.open(image)
        img = img.resize(size)
        tkimage = ImageTk.PhotoImage(img)
        Label(self.root, image=tkimage).place(x=position[0], y=position[1])
    
    def set_button(self, txt, font_param, position, event=None, background=None):
        Button(self.root, text=txt, bg=background, command=event, font=font_param).place(x=position[0],
                                                                                         y=position[1])


if __name__ == "__main__":
    wind = Window(width, heigth, resize, x, y, title, logo)
    wind.build()
    wind.set_image(image="resources/pig.jpg", size=(256, 256), position=(0, 500))
    wind.set_text(txt="HELLO", fg='black', position=(0, 20), font_param=("Arial", 20))
    wind.set_button(txt="click", background='red', position=(0, 50), font_param=("Arial", 12), event=lambda: print('click'))
    wind.run()
