import streamlit as st
from moviepy.editor import VideoFileClip

# Function to convert video to audio
def video_to_audio(video_file):
    video = VideoFileClip(video_file)
    audio_file = video_file.name.replace(".mp4", ".mp3")  # Change the extension to mp3
    audio_file = audio_file.replace(" ", "_")  # Replace spaces with underscores
    audio_file = "temp_" + audio_file  # Prefix with 'temp_' to avoid conflicts in filenames
    video.audio.write_audiofile(audio_file)
    return audio_file

# Function to generate video summary
def generate_summary(audio_file):
    # Implement your video summary generation code using NLP techniques here
    # You can use libraries like spaCy, gensim, or Hugging Face transformers

    # For demonstration purposes, let's just return a dummy summary
    return "This is a dummy video summary."

def main():
    st.title("Video to Audio Converter and Summary Generator")
    
    # Upload video file
    video_file = st.file_uploader("Upload a video", type=["mp4"])

    if video_file is not None:
        st.video(video_file)

        if st.button("Convert Video to Audio"):
            audio_file = video_to_audio(video_file)
            st.success("Video converted to audio successfully!")
            st.audio(audio_file)

            if st.button("Generate Summary"):
                summary = generate_summary(audio_file)
                st.write("Video Summary:")
                st.write(summary)

if __name__ == "__main__":
    main()
