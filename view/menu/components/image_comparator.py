import tkinter as tk
from PIL import Image, ImageTk

from configuration.configuration import Configuration
from view.menu.components.RoundedFrame import RoundedFrame

class ImageComparator(RoundedFrame):
    def __init__(self, master, img_before=None, img_after=None):
        super().__init__(master, 
                bg_color=Configuration.image_comparator_background_color,
                border_color="black",
                corner_radius=20,
                width=master.winfo_screenwidth(),
                height=master.winfo_screenheight(),
                highlightthickness=0)
        
        self.create_widgets()
        
    def create_widgets(self):
        
        self.container = tk.Frame(self, background=Configuration.image_comparator_background_color, width= self.winfo_screenwidth(), height=self.winfo_screenheight())
        self.container.pack(fill="both")
        
        self.frame_before = tk.Frame(self.container, background="red", width= int(self.winfo_screenwidth() / 2), height=self.winfo_screenheight())
        self.frame_before.pack(side=tk.LEFT, fill=tk.Y, padx=1, pady=1)
        # self.container = 