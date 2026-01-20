# Screen Recorder

A lightweight, real-time desktop screen recording tool built with Python. Capture your screen at 60 FPS with live preview and save directly as AVI files.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-0.9.x-yellow)
![License](https://img.shields.io/badge/License-MIT-orange)

## Features

- **Real-time Recording**: Capture your desktop screen at 60 frames per second
- **Live Preview**: Monitor recording with a resizable preview window
- **High Quality**: Record at full HD resolution (1920×1080)
- **Lightweight**: Minimal resource usage with efficient frame processing
- **Simple Controls**: Start/stop with a single key press
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/screen-recorder.git
cd screen-recorder
```

2. **Install Required Packages**
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pyautogui opencv-python numpy
```

3. **Verify Installation**
```bash
python --version
python -c "import cv2; print(f'OpenCV version: {cv2.__version__}')"
```

## Quick Start

Run the recorder with default settings:
```bash
python screen_recorder.py
```

**Default Behavior:**
- Starts recording immediately
- Shows 480×270 preview window
- Saves as `Recording.avi` in current directory
- Press `q` to stop recording

## Usage Guide

### Basic Usage
```python
# Run with default settings
python screen_recorder.py
```

### Advanced Options
Modify these variables in the script for customization:

```python
# Video Settings
resolution = (1920, 1080)  # Change to your screen resolution
fps = 60.0                 # Adjust frame rate (30, 60, etc.)
filename = "Recording.avi" # Custom output filename

# Preview Window
cv2.resizeWindow("Live", 480, 270)  # Change preview size
```

### Controls
- **Start**: Script begins recording immediately on launch
- **Stop**: Press the `q` key in the preview window
- **Preview**: Live feed in resizable window (can be minimized)

## Project Structure

```
screen-recorder/
├── screen_recorder.py     # Main recording script
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
└── examples/             # Usage examples (optional)
```

### Code Breakdown

```python
# Core Components:
1. Screen Capture      - pyautogui.screenshot()
2. Frame Conversion    - RGB to BGR (OpenCV format)
3. Video Encoding      - cv2.VideoWriter with XVID codec
4. Live Preview        - cv2.imshow() with resizable window
5. User Controls       - Keyboard interrupt with 'q' key
```

## Customization

### Change Output Format
```python
# For MP4 format (requires additional codec support)
codec = cv2.VideoWriter_fourcc(*'mp4v')
filename = "Recording.mp4"
```

### Adjust Quality Settings
```python
# Lower quality for smaller files
resolution = (1280, 720)  # HD resolution
fps = 30.0                # Standard frame rate
```

### Record Specific Region
```python
# Modify screenshot capture area
img = pyautogui.screenshot(region=(0, 0, 1920, 1080))  # x, y, width, height
```

## Troubleshooting

### Common Issues

**Issue**: "ModuleNotFoundError" for dependencies
```
Solution: Ensure all packages are installed:
pip install --upgrade pyautogui opencv-python numpy
```

**Issue**: Poor performance or lag
```
Solution: Reduce FPS or resolution:
fps = 30.0
resolution = (1280, 720)
```

**Issue**: Output file won't play
```
Solution: Install media codecs or try different format:
codec = cv2.VideoWriter_fourcc(*'MJPG')
filename = "Recording.mjpeg"
```

**Issue**: Permission errors when saving
```
Solution: Change output directory:
filename = "C:/Users/Public/Videos/Recording.avi"
```

### Performance Tips
- Close unnecessary applications during recording
- Use SSD storage for better write speeds
- Adjust resolution based on your needs
- Monitor disk space for long recordings

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| PyAutoGUI | ≥0.9.53 | Screen capture |
| OpenCV | ≥4.5.0 | Video processing |
| NumPy | ≥1.19.0 | Array operations |
| Pillow | ≥8.0.0 | Image handling (via PyAutoGUI) |

## Limitations

- Records entire screen only (no region selection in current version)
- Output limited to AVI format with XVID codec
- No audio recording capability
- File sizes can be large at high FPS/resolution

## Future Enhancements

Planned features for upcoming versions:
- [ ] Audio recording support
- [ ] Custom recording regions
- [ ] Multiple output formats (MP4, MKV)
- [ ] GUI interface
- [ ] Recording scheduler
- [ ] Cloud storage integration

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

### Development Setup
```bash
# Clone and set up development environment
git clone https://github.com/yourusername/screen-recorder.git
cd screen-recorder
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

