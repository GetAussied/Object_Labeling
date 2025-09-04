Image Annotation Tool

A simple Python GUI tool for manually labeling images with bounding boxes using Tkinter and Pillow (PIL). Designed for creating datasets for object detection tasks.

Features:

Browse and display images from a dataset folder.

Draw and classify objects using bounding boxes.

Assign class labels (e.g., "person") and color-code annotations.

Save annotations in JSON format (database_labels.json) with image paths and bounding boxes.

Prevents duplicate annotations for the same image.

Usage:

Load your image folder.

Click Next Image to browse images.

Draw bounding boxes using left-click to start and right-click to finish and classify.

Save your labels with the Save button.

Ideal for small-scale object detection dataset creation without complex frameworks.

Note:
__main__.py was a solution to my object detection labeling, for easy of use replicate as intended.
