# Image Slideshow Viewer

## Overview
The **Image Slideshow Viewer** is a Python application that displays a slideshow of images in a Tkinter GUI window. It allows users to start a slideshow of images with a button click, cycling through a predefined set of image files at specified intervals.

## Features
- Displays a sequence of images in a slideshow format.
- Resizes images to fit the application window while maintaining aspect ratio.
- A simple and intuitive user interface with a "Play Slideshow" button.

## Prerequisites
Before running the application, ensure you have the following:

### Python Version
- Python 3.7 or later

### Required Libraries
Install the following Python libraries:

- **Pillow**: A Python Imaging Library fork for image processing.
- **Tkinter**: Comes pre-installed with Python for GUI development.

To install Pillow, run:
```bash
pip install pillow
```

## Project Structure
```
image_slideshow/
├── image_slideshow.py  # Main Python script
├── photos/             # Folder containing image files for the slideshow
├── README.md           # Project README file
```

## How to Use

1. **Clone or Download the Repository**:
   ```bash
   git clone <repository_url>
   cd image_slideshow
   ```

2. **Prepare Your Images**:
   - Place your images in the `photos/` directory.
   - Update the `image_paths` list in the `image_slideshow.py` file with the file paths to your images.

3. **Run the Application**:
   Execute the Python script:
   ```bash
   python image_slideshow.py
   ```

4. **Interact with the Application**:
   - Click the "Play Slideshow" button to start the slideshow.
   - The images will cycle every 6 seconds.

## Code Explanation

### Key Components

1. **Image Resizing**:
   The `resize_image` function ensures images fit the target window dimensions while maintaining aspect ratio using `Image.thumbnail()`.

2. **Slideshow Logic**:
   - The `cycle` function from `itertools` is used to iterate through the images indefinitely.
   - `root.after()` schedules updates every 6 seconds without freezing the GUI.

3. **GUI Design**:
   - Built with Tkinter.
   - A `Label` widget displays the images, and a `Button` widget starts the slideshow.

### Functions

- `resize_image(image, size)`:
  Resizes an image to fit within the specified size while maintaining aspect ratio.

- `update_image()`:
  Updates the displayed image at 6-second intervals.

- `start_slideshow()`:
  Starts the slideshow by invoking `update_image()`.

## Notes
- Ensure all image paths are valid. If an image path is incorrect, the application will raise a `FileNotFoundError`.
- Modify the `image_size` variable to adjust the target dimensions for images.
- The interval between image updates can be adjusted by changing the `6000` value in the `root.after()` method (6000 milliseconds = 6 seconds).

## Contributing
Feel free to fork this repository and submit pull requests for any improvements or additional features.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

