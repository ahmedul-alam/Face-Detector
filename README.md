# Face Detector

A real-time face detection application using OpenCV and Haar Cascade classifiers. This project detects faces in a webcam video stream and highlights them with bounding boxes.

## Features

- Real-time face detection from webcam
- Uses Haar Cascade classifier for efficient face detection
- Draws bounding boxes around detected faces
- Simple and lightweight implementation
- Easy to use and modify

## Requirements

- Python 3.x
- OpenCV (cv2)

## Installation

1. Clone the repository or download the files:
```bash
git clone <repository-url>
cd face-detector
```

2. Install the required dependencies:
```bash
pip install opencv-python
```

## Usage

Run the face detector:
```bash
python face-detector.py
```

**Controls:**
- The program will open your webcam and display a live video stream with detected faces highlighted by green rectangles
- Press **'s'** to stop the application
- Press **'q'** or close the window to exit

## How It Works

1. **Video Capture**: Captures frames from the default webcam (device 0)
2. **Grayscale Conversion**: Converts each frame to grayscale for faster processing
3. **Face Detection**: Uses the Haar Cascade classifier to detect faces in the grayscale image
4. **Drawing Rectangles**: Draws green rectangles around each detected face
5. **Display**: Shows the annotated video stream in real-time

## Code Overview

```python
# Initialize Haar Cascade classifier
face_cap = cv2.CascadeClassifier("path/to/haarcascade_frontalface_default.xml")

# Start video capture from webcam
video_capture = cv2.VideoCapture(0)

# Process each frame
while True:
    ret, video = video_capture.read()
    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(video, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("video_live", video)
    if cv2.waitKey(10) == ord('s'):
        break

video_capture.release()
```

## Parameters

- **scaleFactor** (1.1): Factor by which the image size is reduced at each image pyramid level
- **minNeighbors** (5): How many neighbors each candidate rectangle should have to retain it

## Troubleshooting

- **Camera not found**: Ensure your webcam is connected and not in use by another application. Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` if using multiple cameras.
- **Module not found**: Install OpenCV using `pip install opencv-python`
- **Haarcascade file path**: Ensure the path to the Haar Cascade XML file is correct on your system

## Future Enhancements

- Add face recognition capabilities
- Support for multiple face detection algorithms
- Save detected faces to files
- Add adjustable parameters through GUI
- Support for video file input

## License

This project is open source and available for personal and educational use.

## Author

AHMED

## Contributing

Feel free to fork this project, make improvements, and submit pull requests.
