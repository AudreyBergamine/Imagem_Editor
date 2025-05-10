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
        
        self.image_before = tk.Frame(self.container, background="blue", width= self.container.winfo_screenwidth(), height= self.container.winfo_screenmmheight())
        self.image_before.pack(side=tk.LEFT, padx=0, pady=0)
        
        # self.text = tk.Label(self.image_before, text=self.container.winfo_screenheight(), background="blue")
        # self.text.pack(side=tk.TOP, padx=0, pady=0, fill="both")
        
        
        
        # self.container = 