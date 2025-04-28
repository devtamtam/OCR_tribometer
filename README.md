# OCR from MP4

This project extracts numbers from video frames using OCR (Optical Character Recognition). It uses OpenCV and Tesseract for video processing and text recognition.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd OCR_from_mp4
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure Tesseract is installed on your system. For Linux, you can install it using:
   ```bash
   sudo apt-get install tesseract-ocr
   ```

## Usage

1. Place your video file in the `Videos/` directory.

2. Configure the region of interest (ROI) using the `set_roi.py` script:
   ```bash
   python set_roi.py
   ```
   Follow the on-screen instructions to select the ROI using your mouse. Press 's' to save the ROI or 'q' to cancel.

3. Run the main script to extract numbers from the video:
   ```bash
   python main.py
   ```

4. Detected numbers will be printed in the terminal.

## Files

- `main.py`: Main script to extract numbers from video frames.
- `set_roi.py`: Script to help set the region of interest (ROI).
- `roi_config.json`: JSON file to configure the ROI.
- `Videos/`: Directory to store video files.

## Requirements

- Python 3.x
- OpenCV
- Tesseract-OCR
- pytesseract
- pillow

## Notes

- Press `q` to quit the video playback (if applicable).
- Ensure the `roi_config.json` file is correctly configured for accurate OCR results.