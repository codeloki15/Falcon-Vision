#!pip install opencv-python
import cv2
import time
last_capture_time = time.time()
capture_interval = 100  # 100 seconds
current_time = time.time()
time.localtime(current_time)
# Initialize the video capture object with the desired video source
video_source = 0  # Use the default camera (change this to a video file path if needed)
cap = cv2.VideoCapture(video_source)

# Create a variable to keep track of the time when you last captured a frame
last_capture_time = time.time()

# Set the time interval for capturing frames (100 seconds in this case)
capture_interval = 5  # 100 seconds


while True:
    # Capture a frame
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        break

    # Get the current time
    current_time = time.time()

    # Check if it's time to capture a frame (every 100 seconds)
    if current_time - last_capture_time >= capture_interval:
        # Save the frame or process it as needed
        timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime(current_time))
        filename= f"C:/Users/HP/Desktop/lokesh/frame_captured/captured_frame_{timestamp}.jpg"
        # For example, you can save it as an image:
        cv2.imwrite(filename, frame)
        print(f'Frame Saved with filename --> {filename}')

        # Update the last capture time
        last_capture_time = current_time

    # Display the frame (optional)
    cv2.imshow("Frame", frame)

    # Check for user input to exit the loop (e.g., press 'q' to quit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
