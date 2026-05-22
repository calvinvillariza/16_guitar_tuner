# Architecture Overview

## Project Structure

```
guitar-tuner-flask/
├── run.py                      # Entry point - start here!
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview
├── SETUP-WINDOWS.md           # Windows setup guide
├── ARCHITECTURE.md            # This file
│
└── app/
    ├── __init__.py
    ├── main.py                # Flask app factory & routes
    ├── templates/
    │   └── index.html         # Web UI (HTML + CSS + JS)
    └── audio/
        ├── __init__.py
        ├── detector.py        # Pitch detection (future)
        └── processor.py       # Audio analysis (future)
```

## How It Works

### 1. Starting the Application

```
Windows Command Prompt
      ↓
python run.py
      ↓
Flask server starts on http://0.0.0.0:5000
      ↓
      ├─ Local access: http://127.0.0.1:5000
      └─ Network access: http://192.168.1.100:5000
```

### 2. Flask Backend

**app/main.py** creates the Flask app with:

- `GET /` - Serves the main HTML page
- `GET /api/config` - Returns guitar string frequencies
- `GET /api/health` - Health check endpoint
- CORS enabled for cross-origin requests

### 3. Frontend (Browser-Based)

**app/templates/index.html** contains:

- **HTML** - UI structure (buttons, gauge, displays)
- **CSS** - Styling and layout (light/dark mode)
- **JavaScript** - Web Audio API pitch detection
- **Service Worker** - Offline support and caching

## Audio Processing Pipeline

The pitch detection happens **entirely in the browser** using Web Audio API:

```
iPhone Microphone
      ↓
navigator.mediaDevices.getUserMedia()
      ↓
MediaStreamAudioSource (Web Audio API)
      ↓
AnalyserNode (FFT: 4096 samples)
      ↓
getByteFrequencyData()
      ↓
Peak Frequency Detection
      ↓
Calculate Cents Deviation
      ↓
Update Visual Gauge
```

**Why browser-based?**
- Real-time responsiveness (no network latency)
- Privacy (audio never sent to server)
- Offline capability
- Simpler architecture

## Python Backend Role

Currently, Flask serves:
- Static files (HTML, CSS, JS)
- Configuration API (`/api/config`)
- Health checks

Future Python modules (`app/audio/`):
- Server-side pitch analysis
- Audio file processing
- Machine learning improvements
- Data logging and analytics

## Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Server** | Python 3.8+ | Backend runtime |
| **Framework** | Flask 2.3 | Web server & routing |
| **Frontend** | HTML5/CSS3 | UI markup & styling |
| **Audio** | Web Audio API | Pitch detection (browser) |
| **Offline** | Service Worker | Caching & offline support |
| **PWA** | Web App Manifest | Installable on home screen |

## Request Flow

### First Load (iPhone)

```
iPhone Safari                    Flask Server (Windows)
    │                                   │
    ├─────────── GET / ───────────────>│
    │                                   │
    │<─── render_template('index.html')─┤
    │                                   │
    ├─── GET /api/config ─────────────>│
    │                                   │
    │<───── JSON (string frequencies)──┤
    │                                   │
    └─ Service Worker installs cache ──┘
```

### During Tuning (No Server Calls)

```
iPhone Safari                    
    │
    ├─ getUserMedia() → Microphone
    │
    ├─ AudioContext → FFT Analysis
    │
    ├─ Calculate pitch deviation
    │
    └─ Update gauge UI (locally)
    
    No network communication needed!
```

## Key Files Explained

### `run.py` - Entry Point

```python
from app.main import create_app

app = create_app()
app.run(host='0.0.0.0', port=5000, debug=True)
```

**What it does:**
1. Imports the Flask app factory
2. Creates the Flask app
3. Runs on all interfaces (0.0.0.0) so it's accessible on the network

### `app/main.py` - Flask Configuration

```python
def create_app():
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/api/config')
    def get_config():
        return jsonify({'strings': {...}})
```

**What it does:**
1. Creates Flask app instance
2. Enables CORS (allows cross-origin requests)
3. Defines routes and endpoints

### `app/templates/index.html` - Web UI

This single HTML file contains:
- HTML structure
- CSS styling (light/dark mode)
- JavaScript (Web Audio API pitch detection)
- Service Worker registration
- PWA manifest (inline)

**Why single file?**
- Easy deployment
- Self-contained (no separate CSS/JS files)
- Simple to understand

## Browser APIs Used

| API | Purpose | Browser Support |
|-----|---------|-----------------|
| `getUserMedia()` | Microphone access | All modern browsers |
| `AudioContext` | Web Audio processing | All modern browsers |
| `requestAnimationFrame` | 60 FPS animation loop | All modern browsers |
| `Service Worker` | Offline caching | Most modern browsers |
| `Web App Manifest` | PWA installation | iOS 16+, Android, Chrome |

## Data Flow During Tuning

1. **Microphone** → Raw audio samples
2. **FFT** → Frequency spectrum (0-22kHz)
3. **Peak Detection** → Find loudest frequency
4. **Calculation** → Convert to cents deviation
5. **UI Update** → Move gauge needle
6. **Loop** → Repeat at 60 FPS

## Performance Considerations

### CPU Usage
- **Idle:** ~0% (nothing running)
- **Listening:** ~2-5% (FFT + UI updates)
- **Peak:** ~8% (with UI animation)

### Memory
- HTML page: ~50KB
- JavaScript bundle: ~15KB
- FFT buffer: ~2KB
- AudioContext: ~5-10MB (shared)
- **Total:** ~5-10MB

### Network
- First load: ~50KB (HTML + manifest)
- Subsequent loads: Served from Service Worker cache
- During tuning: 0 bytes (all local processing)

## Security

### Permissions
- **Microphone** - Requested per session, can be denied
- **Storage** - Only Service Worker cache (local only)
- **Network** - CORS enabled, no sensitive data transmitted

### HTTPS Requirement
- Production: HTTPS required for `getUserMedia()`
- Development: `localhost` and `127.0.0.1` exempt
- Local network: Check browser policy

### No External Dependencies
- No CDN resources
- No tracking or analytics
- No cookies
- Fully self-contained

## Future Enhancements

### Backend (Python)
- [ ] Tune history/statistics logging
- [ ] Different tuning standards (Drop D, Open G, etc)
- [ ] Calibration API (A4 frequency adjustment)
- [ ] Audio file analysis

### Frontend
- [ ] Chromatic tuner mode
- [ ] Polyphonic tuning (detect multiple strings)
- [ ] Tuning presets
- [ ] User settings persistence

### Infrastructure
- [ ] Docker containerization
- [ ] Deployment to cloud (Heroku, AWS, etc)
- [ ] HTTPS support
- [ ] Analytics dashboard

## Development Workflow

### 1. Local Development
```bash
# Terminal 1: Run Flask server
python run.py

# Terminal 2: Monitor changes
# (Auto-reload is enabled)
```

### 2. Testing on Device
```bash
# Get IP address
ipconfig

# Access on iPhone
http://192.168.1.100:5000
```

### 3. Debugging
- Use iPhone Safari DevTools (Enable in Settings)
- Check Flask console for errors
- Monitor Network tab for API calls

## Deployment Checklist

For production deployment:
- [ ] Set `debug=False` in `run.py`
- [ ] Use proper WSGI server (Gunicorn, uWSGI)
- [ ] Enable HTTPS with SSL certificate
- [ ] Set `SECRET_KEY` environment variable
- [ ] Configure CORS origins properly
- [ ] Add error logging
- [ ] Test on multiple browsers/devices
- [ ] Monitor CPU and memory usage
