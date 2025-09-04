# Image Annotation Tool

A simple **Python GUI tool** for manually labeling images with bounding boxes using **Tkinter** and **Pillow (PIL)**. Designed for creating datasets for object detection tasks.

---

## Features

- Browse and display images from a dataset folder.
- Draw and classify objects using bounding boxes.
- Assign class labels (e.g., `person`) and color-code annotations.
- Save annotations in **JSON format** (`database_labels.json`) with image paths and bounding boxes.
- Prevents duplicate annotations for the same image.

---

## Usage

1. Load your image folder.
2. Click **Next Image** to browse images.
3. Draw bounding boxes:
   - **Left-click** to start the box.
   - **Right-click** to finish the box and classify it.
4. Click **Save** to store your labels in the JSON file.

---

## Notes

- Ideal for small-scale object detection dataset creation without complex frameworks.
- `main.py` is a ready-to-use solution for labeling your dataset. For best results, replicate the setup as intended.
