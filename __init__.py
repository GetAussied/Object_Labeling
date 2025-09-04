import tkinter as tk
import os
import random
import json

from PIL import Image, ImageTk

class selectimage:
    def __init__(self, dataset_root: str):
            self.dataset_root = dataset_root

    def getfolderimages(self, folders: list):
        images = []

        for folder_name in folders:

            directory = os.path.join(self.dataset_root, folder_name)

            images.extend(
                os.path.join(directory,f) for f in os.listdir(directory) if f.lower().endswith((".jpeg", ".jpg", ".png"))
            )

        random.shuffle(images)

        for image in images:
            yield image

    def getrootimages(self):
        images = []

        images.extend(
            os.path.join(self.dataset_root,f) for f in os.listdir(self.dataset_root) if f.lower().endswith((".jpeg", ".jpg", ".png"))
        )

        random.shuffle(images)

        for image in images:
            yield image


class windowsetup:
    def __init__(self):
        self.root = tk.Tk()

        frame = tk.Frame(self.root, padx=10, pady=10)
        canvas = tk.Canvas(self.root)
        
        self.frame = frame.grid()
        self.canvas = canvas
        self.images = []
        self.startpoint = None
        
        # NEW: store labels in memory before writing
        self.current_image_path = None
        self.labels = []
        self.output_file = "database_labels.json"

    def label(self, text: str, column:int, row:int, padx:int, pady:int):
        tk.Label(self.frame, text=text).grid(column=column, row=row, padx=padx, pady=pady)
    
    def button(self, text: str, column:int, row:int, function, padx:int, pady:int):
        tk.Button(self.frame, text=text, command=function).grid(column=column, row=row, padx=padx, pady=pady)

    def image(self, path: str, column:int, row:int, padx:int, pady:int, height:int, width:int):

        if not self.canvas.winfo_ismapped():
            self.canvas.grid(column=column, row=row, padx=padx, pady=pady)

        location = Image.open(path).resize((width, height))
        
        self.photo = ImageTk.PhotoImage(location)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.photo, anchor="nw")
        self.canvas.config(width=width, height=height)

    def classification(self, colour: str, object: str):
        self.canvas.bind("<Button-1>", lambda event: self.onclick_left(event))
        self.canvas.bind("<Button-3>", lambda event: self.onclick_right(event, colour, object))
        self.current_object = object   # track selected class

    def onclick_left(self, event):
        self.startpoint = (event.x, event.y)

    def onclick_right(self, event, colour, object):
        if self.startpoint:
            x1, y1 = self.startpoint
            x2, y2 = event.x, event.y

            # draw rectangle on canvas
            self.canvas.create_rectangle(x1, y1, x2, y2, outline=colour, width=5)
            
            # normalize box coordinates to ensure top-left first
            xmin, xmax = sorted([x1, x2])
            ymin, ymax = sorted([y1, y2])

            # save label in memory
            self.labels.append({
                "class": object,
                "bbox": [xmin, ymin, xmax, ymax]
            })

            self.startpoint = None

    def savelabel(self):
        if not self.current_image_path:
            print("No image loaded.")
            return

        annotation_entry = {
            "image": self.current_image_path,
            "objects": self.labels
        }

        # Load existing data safely
        try:
            with open(self.output_file, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        # Check if this image already exists
        if any(entry["image"] == self.current_image_path for entry in data):
            print(f"Image {self.current_image_path} already saved. Skipping duplicate.")
            return

        # Append new annotation and save
        data.append(annotation_entry)
        with open(self.output_file, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Saved labels for {self.current_image_path}")
        self.labels = []


    def windowcreate(self):
        self.root.mainloop()