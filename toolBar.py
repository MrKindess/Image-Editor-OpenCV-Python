from tkinter import Frame, Button, LEFT, filedialog
from filterFrame import FilterFrame
from adjustFrame import AdjustFrame
import cv2
import numpy as np


class ToolBar(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.new_button = Button(self, text="New")
        self.save_button = Button(self, text="Save")
        self.save_as_button = Button(self, text="Save as")
        self.routate_button = Button(self, text = "Routate")
        self.zoom_in_button = Button(self, text="Zoom in")
        self.zoom_out_button = Button(self, text="Zoom out")
        self.draw_button = Button(self, text="Draw")
        self.crop_button = Button(self, text="Crop")
        self.filter_button = Button(self, text="Filter")
        self.adjust_button = Button(self, text="Adjust")
        self.clear_button = Button(self, text="Clear")

        self.new_button.bind("<ButtonRelease>", self.new_button_released)
        self.save_button.bind("<ButtonRelease>", self.save_button_released)
        self.save_as_button.bind("<ButtonRelease>", self.save_as_button_released)
        self.routate_button.bind("<ButtonRelease>", self.routate_button_released)
        self.zoom_in_button.bind("<ButtonRelease>", self.zoom_in_button_released) 
        self.zoom_out_button.bind("<ButtonRelease>", self.zoom_out_button_released)
        self.draw_button.bind("<ButtonRelease>", self.draw_button_released)
        self.crop_button.bind("<ButtonRelease>", self.crop_button_released)
        self.filter_button.bind("<ButtonRelease>", self.filter_button_released)
        self.adjust_button.bind("<ButtonRelease>", self.adjust_button_released)
        self.clear_button.bind("<ButtonRelease>", self.clear_button_released)
        
        self.new_button.pack(side=LEFT)
        self.save_button.pack(side=LEFT)
        self.save_as_button.pack(side=LEFT)
        self.routate_button.pack(side=LEFT)
        self.zoom_in_button.pack(side=LEFT)
        self.zoom_out_button.pack(side=LEFT)
        self.draw_button.pack(side=LEFT)
        self.crop_button.pack(side=LEFT)
        self.filter_button.pack(side=LEFT)
        self.adjust_button.pack(side=LEFT)
        self.clear_button.pack()

    def new_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.new_button:
            filename = filedialog.askopenfilename()
            image = cv2.imread(filename)

            if image is not None:
                self.x1 = 1
                self.y1 = 1
                self.master.filename = filename
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                self.zoom_image = self.master.processed_image
                self.routate_image = self.master.processed_image
                self.master.image_viewer.show_image()
                self.master.is_image_selected = True
    
    def save_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_button:
            if self.master.is_image_selected:
                save_image = self.master.processed_image
                image_filename = self.master.filename
                cv2.imwrite(image_filename, save_image)

    def save_as_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
            if self.master.is_image_selected:
                save_image = self.master.processed_image
                filename_extension = self.master.filename.split('.')[-1]
                filename = filedialog.askopenfilename()
                filename = filename + '.' + filename_extension
                cv2.imwrite(filename, save_image)
    def routate_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
            if self.master.is_image_selected:
                self.master.processed_image = np.rot90(self.routate_image)
                self.master.image_viewer.show_image()

    # def zoom_in(frame1, x, y):
    #     return cv2.resize(frame1, (0, 0), fx=x, fy=y)
    # def show_image(self):
    #     self.master.image_viewer.show_image(img=self.master.processed_image)

    def zoom_in_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.zoom_in_button:
            if self.master.is_image_selected:
                if self.x1 <= 2 or self.y1 <= 2:
                    self.x1+=0.1
                    self.y1+=0.1
                    self.master.processed_image = cv2.resize(self.zoom_image, (0, 0), fx=self.x1, fy=self.y1)
                    self.master.image_viewer.show_image()


    def zoom_out_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.zoom_out_button:
            if self.master.is_image_selected:
                self.x1-=0.1
                self.y1-=0.1
                self.master.processed_image = cv2.resize(self.zoom_image, (0, 0), fx=self.x1, fy=self.y1)
                self.master.image_viewer.show_image()
    
    def draw_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.draw_button:
            if self.master.is_image_selected:
                self.master.image_viewer.activate_draw()
    
    def crop_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.crop_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                else:
                    self.master.image_viewer.activate_crop()

    def filter_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.filter_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.filter_frame = FilterFrame(master=self.master)
                self.master.filter_frame.grab_set()

    def adjust_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.adjust_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.adjust_frame = AdjustFrame(master=self.master)
                self.master.adjust_frame.grab_set()
    
    def clear_button_released(self, event):
                if self.winfo_containing(event.x_root, event.y_root) == self.clear_button:
                    if self.master.is_image_selected:
                        self.master.processed_image = self.master.original_image.copy()
                        self.master.image_viewer.show_image()


    
