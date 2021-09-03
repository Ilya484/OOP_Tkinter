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
        self.font = None
        self.root = Tk()
    
    def build(self):
        self.root.geometry(f"{self.width}x{self.heigth}"
                           f"+{self.xpos}+{self.ypos}")
        self.root.resizable(*self.tranform)
        self.root.iconbitmap(default=self.logo)
        self.root.title(self.title)
    
    def run(self):
        self.root.mainloop()
    
<<<<<<< Updated upstream
    def set_text(self, txt, fg, position, font, rel=None, textvar=None, bg=None):
        Label(self.root, text=txt, background=bg, foreground=fg, font=font, textvariable=textvar, relief=rel).place(x=position[0],
                                                                                        y=position[1])
=======
    def set_text(self, txt=None, fg="black", position=(0,0), font=None, rel=None, textvar=None, bg=None):
        Label(self.root, text=txt, background=bg, foreground=fg, font=font, textvariable=textvar, relief=rel).place(
            x=position[0],
            y=position[1])
>>>>>>> Stashed changes
    
    def set_image(self, image=None, size=None, position=(0,0)):
        global tkimage
        img = Image.open(image)
        img = img.resize(size)
        tkimage = ImageTk.PhotoImage(img)
        Label(self.root, image=tkimage).place(x=position[0], y=position[1])
    
    def set_button(self, txt=None, font=None, position=(0, 0), event=None, background=None):
        Button(self.root, text=txt, bg=background, command=event, font=font).place(x=position[0],
                                                                                         y=position[1])