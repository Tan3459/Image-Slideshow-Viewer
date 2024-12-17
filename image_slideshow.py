from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

# Initialize Tkinter
root = tk.Tk()
root.title("Image Slideshow Viewer")

# Set the dimensions of the Tkinter window
window_size = (1080, 740)
root.geometry(f"{window_size[0]}x{window_size[1]}")

# List of image paths
image_paths = [
    r"D:\Python Project\image slideshow\photos\20241028_083617.jpg",
    r"D:\Python Project\image slideshow\photos\20241110_122330.jpg",
    r"D:\Python Project\image slideshow\photos\20241110_122338.jpg",
    r"D:\Python Project\image slideshow\photos\20241110_132728(0).jpg",
    r"D:\Python Project\image slideshow\photos\20241112_101049.jpg"
]

# Resize and scale images to fit the window dimensions
image_size = (1080, 740)  # Target display size for the images


def resize_image(image, size):
    """Resize an image to fit within the target size while maintaining aspect ratio."""
    image.thumbnail(size, Image.Resampling.LANCZOS)
    return image


# Load and resize images
images = [resize_image(Image.open(path), image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

# Tkinter Label to display images
label = tk.Label(root)
label.pack(fill="both", expand=True)  # Make the label fill the entire window

# Slideshow logic using a generator
slideshow = cycle(photo_images)


def update_image():
    """Update the displayed image."""
    photo_image = next(slideshow)  # Get the next image
    label.config(image=photo_image)  # Update the label with the image
    root.after(6000, update_image)  # Schedule the next image update after 6 seconds


def start_slideshow():
    """Start the slideshow."""
    update_image()  # Start updating images


# Add a button to start the slideshow
play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()

# Run the Tkinter event loop
root.mainloop()
