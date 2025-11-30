# 🚗 BrakeBots – AI-Based Automatic Braking System

A Python + Computer Vision project that detects sudden high-intensity motion (accident-like patterns) using real-time video analysis and triggers an **automatic braking warning system**.

This project simulates the core logic used in early ADAS (Advanced Driver Assistance Systems) such as automatic emergency braking (AEB), collision alerts, and motion-based safety systems.

---

## 🔥 Features

* 🎯 **Real-time Accident Detection** using motion intensity spikes
* 📉 **Background Subtraction (MOG2)** to isolate moving objects
* 🧹 **Noise Removal** using morphological filtering (5×5 kernel)
* 📦 **Contour-Based Motion Analysis**
* ⚠️ **Brake Warning System** when threshold is exceeded
* 🧪 Works on any video input (CCTV, dashcam, traffic footage)

---

## 🧠 How It Works

1. The video is processed frame-by-frame.
2. Background Subtraction (MOG2) identifies moving objects.
3. A morphological kernel cleans noise.
4. Contours are detected and their combined area is calculated.
5. A sudden spike in motion area = **collision/impact**.
6. The system overlays **ACCIDENT WARNING! BRAKE APPLIED** on the video frame.

---

## 🛠️ Tech Stack

* Python
* OpenCV
* NumPy
* Background Subtractor MOG2
* Contour + Area Motion Analysis

---

## 📂 Project Code (Core Logic)

```python
if motion_intensity > ACCIDENT_THRESHOLD * 1000:
    cv2.putText(frame, "ACCIDENT WARNING! BRAKE APPLIED", (100,180),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 5)
```

---

## 👥 Team BrakeBots

* Sparsh Prachandia Jain — Team Lead & System Architect
* Chinmay Jain — Computer Vision Engineer
* Divyansh Sharma — AI Logic & Algorithm Developer
* Parv Kashyap — Testing & QA Lead
* Pratyush Anand — Documentation & Workflow Designer

---

## 🚀 Future Enhancements

* YOLO-based Object Detection
* Depth estimation for real braking distance
* Hardware integration (Raspberry Pi + sensors)
* Live camera support
* ADAS-style dashboard UI

---

## 📜 License

This project is for educational and research purposes.

---

## ⭐ If you like this project…

Consider giving the repository a **star** ⭐ on GitHub to support Team BrakeBots!
