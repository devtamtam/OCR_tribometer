import json
import cv2

# Global variables for mouse callback
roi_coords = []
drawing = False

# Mouse callback function to draw rectangle
def draw_rectangle(event, x, y, flags, param):
    global roi_coords, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        roi_coords = [(x, y)]

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp_frame = param.copy()
            cv2.rectangle(temp_frame, roi_coords[0], (x, y), (0, 255, 255), 2)
            cv2.imshow("Set ROI", temp_frame)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        roi_coords.append((x, y))
        cv2.rectangle(param, roi_coords[0], roi_coords[1], (0, 255, 255), 2)
        cv2.imshow("Set ROI", param)

# Function to set ROI using GUI and save to JSON
def set_roi_and_save(config_path, json_path):
    # Load video path from config file
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    video_path = config["video_path"]

    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read video.")
        cap.release()
        return

    cv2.namedWindow("Set ROI")
    cv2.setMouseCallback("Set ROI", draw_rectangle, frame)

    while True:
        cv2.imshow("Set ROI", frame)
        key = cv2.waitKey(1) & 0xFF

        # Press 'q' to quit or 's' to save ROI
        if key == ord('q'):
            print("ROI selection canceled.")
            roi_coords.clear()
            break
        elif key == ord('s') and len(roi_coords) == 2:
            print(f"ROI set to: {roi_coords}")
            break

    cv2.destroyAllWindows()
    cap.release()

    if len(roi_coords) == 2:
        top_left = roi_coords[0]
        bottom_right = roi_coords[1]
        roi_data = {
            "top": top_left[1],
            "bottom": bottom_right[1],
            "left": top_left[0],
            "right": bottom_right[0]
        }
        with open(json_path, 'w') as json_file:
            json.dump(roi_data, json_file, indent=4)
        print(f"ROI saved to {json_path}")

if __name__ == "__main__":
    config_path = "config.json"  # Path to the JSON file with video path
    json_path = "roi_config.json"  # Replace with your desired JSON file path
    set_roi_and_save(config_path, json_path)