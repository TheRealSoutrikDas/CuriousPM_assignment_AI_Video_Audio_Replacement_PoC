from moviepy.editor import VideoFileClip, AudioFileClip

def extract_audio(video_file_path):
    video_clip = VideoFileClip(video_file_path)
    audio_path = "temp_audio.wav"
    video_clip.audio.write_audiofile(audio_path)
    return audio_path

def replace_audio(video_file_path, new_audio_path):
    video_clip = VideoFileClip(video_file_path)
    new_audio_clip = AudioFileClip(new_audio_path)
    
    final_clip = video_clip.set_audio(new_audio_clip)
    final_output_path = "final_video.mp4"
    final_clip.write_videofile(final_output_path)
    return final_output_path