import os
import gradio as gr

from Logic import encode_image, analyze_image_with_query
from Voice_Input import record_audio, transcribe_with_groq
from Voice_Output import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

system_prompt = """You have to act as a professional doctor, I know you are not, but this is for learning purposes. 
            If the image is NOT related to medical or health issues (e.g., a plant, animal, object, or non-medical content), respond with "I can only provide medical insights. Please provide a health-related image or question."
            What's in this image? Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Do not add any numbers, bullet points, or special characters in 
            your response. Your response should be in one paragraphs and less than 100 words. Also, always answer as if you are answering a real person.
            Do not say 'In the image I see' but say 'With what I see, I think you have ....'
            Don't respond as an AI model in markdown; your answer should mimic that of an actual doctor, not an AI bot. 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away, please."""


def process_inputs(audio_filepath, image_filepath, text_input):
    # If text input is provided, use it instead of speech-to-text
    if text_input.strip():
        query = text_input
    else:
        query = transcribe_with_groq(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
            audio_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + query, 
            encoded_image=encode_image(image_filepath), 
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = text_to_speech_with_elevenlabs(input_text=doctor_response, output_filepath="final.mp3")

    return query, doctor_response, voice_of_doctor


# Interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Voice Input"),
        gr.Image(type="filepath", label="Medical Image (Optional)"),
        gr.Textbox(label="Text Input (Alternative to Voice)")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text / Text Query"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio("final.mp3", label="Voice Response")
    ],
    title="HELIX: AI Doctor with Vision, Voice, and Text"
)

iface.launch(debug=True)


#127.0.0.