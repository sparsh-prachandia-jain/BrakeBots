import cv2
import numpy as np

# ----------- SETTINGS -----------
VIDEO_PATH = "accident_video-3.mp4"
ACCIDENT_THRESHOLD = 20  # sensitivity (lower → more sensitive)
# --------------------------------

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("[ERROR] Could not open the video file. Check name/path.")
    exit()

# Background subtractor (AI-like motion segmentation)
backSub = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=40)

accident_detected = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for better speed
    frame = cv2.resize(frame, (900, 500))

    # Apply background subtraction
    fgMask = backSub.apply(frame)

    # Reduce noise
    kernel = np.ones((5, 5), np.uint8)
    fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_OPEN, kernel)

    # Find contours (moving objects)
    contours, _ = cv2.findContours(fgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate motion intensity
    motion_intensity = sum(cv2.contourArea(cnt) for cnt in contours)

    # --- Simple AI logic for accident detection ---
    # Logic: sudden large increase in motion = impact/collision
    if motion_intensity > ACCIDENT_THRESHOLD * 1000:  
        accident_detected = True
        cv2.putText(frame, "ACCIDENT WARNING! BRAKE APPLIED", (100, 180),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 5)

    else:
        accident_detected = False

    # Draw motion intensity on screen
    cv2.putText(frame, f"Motion Level: {int(motion_intensity)}", (50, 470),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    # Display the video
    cv2.imshow("AI Accident Detection", frame)

    # Exit key
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
