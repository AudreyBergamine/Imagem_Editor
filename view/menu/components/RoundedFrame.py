import tkinter as tk

class RoundedFrame(tk.Canvas):
    def __init__(self, master, bg_color="#555", border_color="black", corner_radius=20, **kwargs):
        super().__init__(master, **kwargs)
        self._bg_color = bg_color
        self._border_color = border_color
        self._corner_radius = corner_radius
        
        self.bind('<Configure>', self._on_resize)
        
    def _on_resize(self, event):
        self.delete("round_rectangle")
        width = event.width
        height = event.height
        
        # Desenha o retângulo com cantos arredondados
        self.create_rounded_rectangle(0, 0, width, height, 
                                    radius=self._corner_radius, 
                                    fill=self._bg_color,
                                    outline=self._border_color,
                                    width=10,
                                    tags="round_rectangle")

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)
