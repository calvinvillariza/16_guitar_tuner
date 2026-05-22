# Guitar Tuner Flask App

A web-based guitar tuner PWA built with Flask backend and Web Audio API frontend. Installable on iOS 16+, Android, and desktop browsers.

## Features

- Real-time pitch detection using Web Audio API
- Tune all 6 guitar strings (E, A, D, G, B, E)
- Progressive Web App (installable on home screen)
- Works offline with Service Worker
- Light/dark mode support
- iOS 16+ compatible
- Access from iPhone on local network

## Quick Start

### 1. Install Python 3.8+

Download from https://www.python.org/downloads/

### 2. Setup Project

```bash
# Navigate to project directory
cd 16_guitar_tuner

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### WSL2

# setup port forwarding

netsh interface portproxy add v4tov4 listenport=5000 listenaddress=0.0.0.0 connectport=5000 connectaddress=127.0.0.1

### 3. Run the Server

```bash
python run.py
```

You'll see:

```
 * Running on http://127.0.0.1:5000
 * To access from other devices on your network:
   http://192.168.X.X:5000
```

### 4. Access from iPhone

1. Copy your computer's IP (e.g., `192.168.1.100`)
2. On iPhone Safari: `http://192.168.1.100:5000`
3. Tap Share → "Add to Home Screen" to install

## Project Structure

```
16_guitar_tuner/
├── run.py                 # Entry point
├── requirements.txt       # Python dependencies
├── README.md
├── app/
│   ├── __init__.py
│   ├── main.py           # Flask app factory
│   ├── templates/
│   │   └── index.html    # Web UI
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── app.js
│   └── audio/
│       ├── __init__.py
│       ├── detector.py   # Pitch detection logic
│       └── processor.py  # Audio analysis
└── docs/
    ├── ARCHITECTURE.md
    ├── SETUP-WINDOWS.md
    └── API.md
```

## Technology Stack

- **Backend:** Python 3.8+, Flask 2.3
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Audio:** Web Audio API (browser-based)
- **PWA:** Service Worker, Web App Manifest
- **Cross-origin:** Flask-CORS

## API Endpoints

- `GET /` - Main app page
- `GET /api/config` - App configuration (string frequencies, etc)
- `GET /health` - Health check
- Future: Audio analysis endpoints for backend processing

## Browser Support

| Browser | iOS | Android | Desktop |
| ------- | --- | ------- | ------- |
| Safari  | 16+ | —       | 14+     |
| Chrome  | —   | 9+      | 25+     |
| Firefox | —   | 4+      | 25+     |
| Edge    | —   | —       | 18+     |

## Development

### File Structure Reference

- **run.py** - Start here. Entry point that runs the Flask server
- **app/main.py** - Flask app initialization and routes
- **app/templates/index.html** - HTML template with embedded CSS and JS
- **app/audio/detector.py** - Python pitch detection (future use)
- **app/audio/processor.py** - Audio processing utilities (future use)

### Next Steps

1. Understand the basic Flask setup
2. Run locally on Windows
3. Test on iPhone with local server
4. Extend with additional features

## Troubleshooting

**"ModuleNotFoundError: No module named 'flask'"**

- Make sure virtual environment is activated
- Run: `pip install -r requirements.txt`

**iPhone can't connect**

- Both devices must be on same WiFi
- Check firewall settings
- Verify IP address with `ipconfig` (Windows) or `ifconfig` (Mac/Linux)

**Port 5000 already in use**

- Edit `run.py` and change `port=5000` to `port=5001`

## License

MIT License
