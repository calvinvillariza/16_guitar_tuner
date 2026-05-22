# Setup Guide - Windows 11

## Prerequisites

- Windows 11
- Python 3.8 or higher
- iPhone or another device on your WiFi network

## Step 1: Install Python

1. Download Python from https://www.python.org/downloads/
2. **Important:** Check "Add Python to PATH" during installation
3. Click "Install Now"
4. Verify installation by opening Command Prompt and typing:
   ```bash
   python --version
   ```

## Step 2: Setup the Project

1. **Extract the project** to a folder, e.g., `C:\Users\YourName\Documents\guitar-tuner-flask`

2. **Open Command Prompt** in the project directory:
   - Hold Shift and right-click inside the folder
   - Select "Open PowerShell window here"

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**
   ```bash
   venv\Scripts\activate
   ```
   
   You should see `(venv)` at the start of the command line.

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Step 3: Run the Server

With the virtual environment activated, run:

```bash
python run.py
```

You'll see output like:
```
 * Running on http://127.0.0.1:5000
```

## Step 4: Find Your Computer's IP Address

Open a **new** Command Prompt and type:

```bash
ipconfig
```

Look for "IPv4 Address" under your WiFi network. It should look like:
```
IPv4 Address . . . . . . . . . . . : 192.168.1.100
```

Note this IP address.

## Step 5: Access from iPhone

1. On your iPhone, open **Safari**
2. Type in the address bar:
   ```
   http://192.168.1.100:5000
   ```
   (Replace `192.168.1.100` with your actual IP from Step 4)

3. Press "Go"

4. The tuner should load. **Tap Share (↗) → "Add to Home Screen"** to install it as an app.

## Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"

- Make sure you activated the virtual environment (you should see `(venv)` in the terminal)
- Run: `pip install -r requirements.txt`

### iPhone can't connect to the server

1. **Check WiFi:** Both devices must be on the **same WiFi network**
2. **Check firewall:** Windows Firewall might block the connection
   - Press `Win + R`, type `firewall.cpl`, press Enter
   - Click "Allow an app through firewall"
   - Find Python (or add it) and enable it
3. **Check IP address:** Run `ipconfig` again and verify the IP
4. **Try a different port:** Edit `run.py` and change `port=5000` to `port=8000`

### "Port 5000 already in use"

Edit `run.py`:
```python
app.run(
    host='0.0.0.0',
    port=5001,        # Change 5000 to 5001
    debug=True,
    use_reloader=True
)
```

Then access: `http://192.168.1.100:5001`

### Microphone not working on iPhone

1. Go to **Settings → Privacy → Microphone**
2. Find **Safari** and make sure it's enabled
3. Go back to the tuner app and reload the page

## Keeping the Server Running

- **Keep the Command Prompt window open** while you use the tuner
- To stop the server, press `Ctrl + C` in the Command Prompt
- To start again, activate venv and run `python run.py` again

## Tips

- The server runs on `0.0.0.0:5000` which makes it accessible on your entire network
- If you close the Command Prompt, the server stops
- Both devices (Windows PC and iPhone) must be on the same WiFi for this to work
- The app works offline after the first load thanks to the Service Worker

## Next Steps

Once it's running:
1. Test the tuner on your iPhone
2. Try adding it to your home screen
3. Test offline functionality
4. Explore the Python backend code in `app/main.py`
