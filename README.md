# 🎙️ AI Voice Assistant

A Python-based voice assistant that listens to your spoken commands, processes them, and responds with speech. It can tell the time, date, weather, open applications, and perform web searches — all hands-free.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🗣️ **Voice Recognition** | Converts speech to text using Google Speech Recognition |
| 🔊 **Text-to-Speech** | Responds with natural-sounding voice output |
| 🕐 **Time & Date** | Tells the current time and date on request |
| 🌤️ **Weather Updates** | Fetches real-time weather data for any city (OpenWeatherMap API) |
| 📂 **App Launcher** | Opens system applications like Notepad and Calculator |
| 🔍 **Web Search** | Performs Google searches from voice commands |
| 👋 **Smart Greeting** | Greets the user based on the time of day |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Speech Recognition:** `SpeechRecognition` + `PyAudio`
- **Text-to-Speech:** `pyttsx3`
- **Weather API:** OpenWeatherMap
- **Web Search:** `webbrowser` (standard library)

---

## 📋 Prerequisites

- Python 3.8 or higher
- A working microphone
- Internet connection (for speech recognition and weather data)

---

## 🚀 Installation

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/your-username/ai-voice-assistant.git
   cd ai-voice-assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Set up Weather API:**
   - Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Open `voice_assistant.py` and replace `"demo"` with your API key:
     ```python
     api_key = "your_api_key_here"
     ```

---

## ▶️ Usage

Run the assistant:

```bash
python voice_assistant.py
```

The assistant will greet you and start listening for commands.

### 🎤 Supported Voice Commands

| Say this... | What happens |
|-------------|--------------|
| *"What time is it?"* | Tells the current time |
| *"What's the date?"* | Tells today's date |
| *"What's the weather?"* | Asks for a city, then gives the weather report |
| *"Open Notepad"* | Opens Notepad |
| *"Open Calculator"* | Opens Calculator |
| *"Search for Python tutorials"* | Opens a Google search in your browser |
| *"Exit" / "Quit" / "Stop"* | Shuts down the assistant |

---

## 📁 Project Structure

```
ai voice assistance/
├── voice_assistant.py    # Main application with all assistant logic
├── test_microphone.py    # Utility to test microphone setup
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🧪 Testing Your Microphone

If you're having microphone issues, run the test script first:

```bash
python test_microphone.py
```

This will verify that your microphone is detected and working properly.

---

## ⚙️ Dependencies

```
speechrecognition
pyttsx3
requests
pyaudio
```

> **Note (Windows):** If `PyAudio` fails to install, try:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## 🔮 Future Enhancements

- [ ] Add support for more applications
- [ ] Integrate with a conversational AI (e.g., Gemini, GPT)
- [ ] Add music playback support
- [ ] Implement reminder and alarm features
- [ ] Add multi-language support

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

<p align="center">Made with ❤️ using Python</p>
