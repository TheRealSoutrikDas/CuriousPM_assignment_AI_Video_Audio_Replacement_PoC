from google.cloud import speech

def transcribe_audio(audio_file_path):
    client = speech.SpeechClient()
    
    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()
    
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US"
    )
    
    response = client.recognize(config=config, audio=audio)
    
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript
    return transcription