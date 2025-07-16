# MediBuddy: AI Doctor with Vision, Voice, and Text

**MediBuddy** is a multimodal AI-powered virtual doctor that takes **voice**, **image**, or **text** inputs and provides concise medical feedback. This tool is designed for learning and experimentation purposes and mimics how a real doctor might respond—based on image analysis and a health-related query.

> ⚠️ This application is **not a replacement for real medical advice**. It is intended strictly for educational and demo use only.

## 🚀 Features

* 🎧 Voice input with Whisper STT (via GROQ API)
* 🖼️ Medical image analysis using LLaMA-4 via Meta API
* 📅 Text-based query support as an alternative to voice
* 🧠 Smart system prompt that generates natural, doctor-like responses
* 🔊 Voice output using ElevenLabs TTS

## 🧠 Technologies Used

* **Gradio** for the user interface
* **GROQ API** for transcription using `whisper-large-v3`
* **Meta LLaMA-4** for image + text-based medical analysis
* **ElevenLabs** for text-to-speech (doctor voice)
* **Python** (with modular logic files)

## 🛠️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/pg-gosavi/MediBuddy.git
cd MediBuddy/Test_MediBuddy
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Set Environment Variables**

Add to `.env` or export manually:

```bash
export GROQ_API_KEY=your_groq_api_key
```

4. **Run the App**

```bash
python app.py
```

## 💡 How It Works

1. User provides input via:

   * 🎧 Microphone (voice)
   * 📝 Textbox
   * 🖼️ Medical image (optional)
2. The system transcribes voice or uses the typed input.
3. Image and query are sent to Meta's LLaMA model via the `analyze_image_with_query()` method.
4. A short, human-like doctor response is generated.
5. The response is converted into speech using ElevenLabs and returned via Gradio interface.

## 🔮 Example Use Cases

* Upload a skin rash image and ask:
  “What’s wrong with this?”
* Speak:
  “What could be the issue with this chest X-ray?”
* Type:
  “Is this swelling dangerous?” and upload a relevant image.

## 🧠 AI Prompt Behavior

The system prompt is designed to:

* Respond like a **real doctor**, not an AI bot.
* Give short, **2-sentence max** answers.
* Avoid markdown, lists, or preambles.
* Politely decline if the image is not health-related.

Sample logic from `app.py`:

```python
system_prompt = """You have to act as a professional doctor...
...Keep your answer concise (max 2 sentences). No preamble, start your answer right away, please."""
```

## 📅 Notes

* **Text input overrides voice input** if both are provided.
* **Image is optional**, but required for LLaMA to return relevant medical insight.
* Voice responses are saved as `final.mp3`.

## 🙋‍♂️ Author

**Parth Gosavi**
GitHub: [@pg-gosavi](https://github.com/pg-gosavi)

## 📌 Disclaimer

This project is for **educational purposes only**.
Do **not** use HELIX for real-world diagnosis or treatment.

