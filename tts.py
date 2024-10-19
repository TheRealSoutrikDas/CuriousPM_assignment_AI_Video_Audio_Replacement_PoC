from google.cloud import texttospeech

def text_to_speech(text):
    client = texttospeech.TextToSpeechClient()
    
    input_text = texttospeech.SynthesisInput(text=text)
    
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-JennyNeural",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )
    
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    
    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )
    
    audio_path = "output_audio.mp3"
    with open(audio_path, "wb") as out:
        out.write(response.audio_content)
    return audio_path