import tkinter as tk
from PIL import Image, ImageTk

from configuration.configuration import Configuration
from view.menu.components.RoundedFrame import RoundedFrame
 
class ImageComparator(RoundedFrame):
    def __init__(self, master, img_before=None, img_after=None):
        super().__init__(master, 
                bg_color=Configuration.image_comparator_background_color,
                border_color="red",
                corner_radius=20,
                
                highlightthickness=0)
        
        self.master = master
        self.create_widgets()
         
    def create_widgets(self):
        
        
        self.container = tk.Frame(self, background="green")
        self.container.pack(fill="both", padx=10, pady=10)
        
        
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        
        self.image_before = tk.Frame(self.container, background="blue", height=self.container.winfo_screenheight())
        self.image_before.pack_forget()
        self.image_before.grid(row=0, column=0, sticky="nsew", padx=2)
        
        self.image_after = tk.Frame(self.container, background="gray", height=self.container.winfo_screenheight())
        self.image_after.pack_forget()
        self.image_after.grid(row=0, column=1, sticky="nsew", padx=2)
        