import streamlit as st
from video_processing import extract_audio, replace_audio
from transcription import transcribe_audio
from correction import correct_transcription
from tts import text_to_speech

def main():
    st.title("AI-based Video Audio Replacement")
    
    video_file = st.file_uploader("Upload a Video File", type=["mp4", "mov"])
    
    if video_file:
        st.video(video_file)
        if st.button("Process Video"):
            process_video(video_file)

def process_video(video_file):

    video_path = f"temp_video.mp4"
    with open(video_path, "wb") as f:
        f.write(video_file.getbuffer())
    
    audio_path = extract_audio(video_path)
    transcription = transcribe_audio(audio_path)
    st.write("Original Transcription:", transcription)
    corrected_text = correct_transcription(transcription)
    st.write("Corrected Text:", corrected_text)
    new_audio_path = text_to_speech(corrected_text)
    final_video_path = replace_audio(video_path, new_audio_path)
    
    st.video(final_video_path)

if __name__ == '__main__':
    main()