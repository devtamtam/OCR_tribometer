import cv2
import pytesseract
import json

def play_video_and_extract(video_path, config_path):
    cap = cv2.VideoCapture(video_path)

    # Load ROI configuration from JSON file
    with open(config_path, 'r') as json_file:
        roi_config = json.load(json_file)

    top = roi_config["top"]
    bottom = roi_config["bottom"]
    left = roi_config["left"]
    right = roi_config["right"]

    previous_number = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Display the video frame
        cv2.imshow('Video Playback', frame)

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

        # Exit playback if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Load video path from config.json
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    video_path = config["video_path"]  # Path to the video file
    config_path = "roi_config.json"  # Path to the JSON file with ROI configuration

    # Run video playback and OCR extraction in real-time
    play_video_and_extract(video_path, config_path)