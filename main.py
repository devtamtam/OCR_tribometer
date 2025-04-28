import cv2
import pytesseract
import json

# Function to extract numbers from video frames
def extract_numbers_from_video(video_path, config_path):
    # Load ROI configuration from JSON file
    with open(config_path, 'r') as json_file:
        roi_config = json.load(json_file)

    top = roi_config["top"]
    bottom = roi_config["bottom"]
    left = roi_config["left"]
    right = roi_config["right"]

    cap = cv2.VideoCapture(video_path)
    previous_number = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Crop the frame to the specified region of interest (ROI)
        roi_frame = frame[top:bottom, left:right]

        # Convert frame to grayscale for better OCR accuracy
        gray_frame = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2GRAY)

        # Use Tesseract to extract text from the frame
        text = pytesseract.image_to_string(gray_frame, config='--psm 7')

        # Extract numbers from the text
        numbers = ''.join(filter(str.isdigit, text))

        if numbers and numbers != previous_number:
            print(f"Detected number: {numbers}")
            previous_number = numbers

    cap.release()

if __name__ == "__main__":
    video_path = "./Videos/IOHD0085.MP4"  # Replace with your video path
    config_path = "roi_config.json"  # Path to the JSON file with ROI configuration

    # Run the OCR extraction
    extract_numbers_from_video(video_path, config_path)