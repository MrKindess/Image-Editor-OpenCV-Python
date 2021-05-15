import tkinter as tk
from tkinter import ttk
from toolBar import ToolBar
from viewer import Viewer


class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.filename = None
        self.origin_image = None
        self.processed_image = None
        self.filter_frame = None
        self.adjust_frame = None
        self.is_image_select = False
        self.is_draw_state = False
        self.is_crop_state = False
        self.x1 = 1
        self.y1 = 1
        
        self.title("Image Editor")

        self.toolbar = ToolBar(master=self)
        separator1 = ttk.Separator(master=self, orient=tk.HORIZONTAL)
        self.image_viewer = Viewer(master=self)

        self.toolbar.pack(pady=10)
        separator1.pack(fill=tk.X, padx=20, pady=5)
        self.image_viewer.pack(fill=tk.BOTH, padx=20, pady=10, expand=1)


        
