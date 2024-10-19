AI Video Audio Replacement PoC

This project is a Proof of Concept (PoC) that processes a video file, transcribes its audio, corrects grammatical mistakes using OpenAI's GPT-4 model, and finally replaces the original audio with a synthesized AI voice.

Features:

Transcribes video audio using Google Speech-to-Text API.

Uses OpenAI GPT-4 model to correct grammatical mistakes in the transcription.

Converts the corrected text back to audio using Google Text-to-Speech API (using the Journey voice model).

Replaces the original video audio with the new AI-generated voice.



---

Prerequisites

Before setting up and running the project, ensure you have the following:

Python 3.7+

Google Cloud account with access to Speech-to-Text and Text-to-Speech APIs.

OpenAI GPT-4 API key (provided via Azure OpenAI or OpenAI directly).

ffmpeg installed (for handling video and audio file manipulation).

Streamlit for creating the web-based PoC interface.


Required Python Libraries:

openai (for GPT-4 model)

google-cloud-speech (for Speech-to-Text API)

google-cloud-texttospeech (for Text-to-Speech API)

pydub (for audio file manipulation)

moviepy (for video processing)

streamlit (for creating the web app)



---

Setup Instructions

1. Clone the repository

2. Set up Google Cloud Services

A. Enable Speech-to-Text and Text-to-Speech APIs

1. Visit the Google Cloud Console.


2. Create a new project or select an existing one.


3. Enable the following APIs for your project:

Speech-to-Text API

Text-to-Speech API




B. Create a Service Account and Download Credentials

1. In the Google Cloud Console, go to IAM & Admin > Service Accounts.


2. Create a new service account and assign it the roles:

Speech-to-Text User

Text-to-Speech User



3. Create and download a JSON key file for this service account.



C. Set the Service Account Key Path

In your project, add the following line to set the path to your Google credentials:

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/google_credentials.json"

Make sure to replace "path/to/your/google_credentials.json" with the actual path to the file you downloaded.

3. Set up the environment

A. Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

B. Install dependencies

pip install -r requirements.txt

4. Set up OpenAI GPT-4 API Key

To use the GPT-4 model, you will need an OpenAI API key. You can either:

Sign up for OpenAI via Azure OpenAI Services.

Or get your API key directly from OpenAI.


Set your OpenAI API key as an environment variable:

set OPENAI_API_KEY="your_openai_api_key"


---

Running the Project

1. Streamlit Web App

To launch the PoC web app with Streamlit, run:

streamlit run app.py

2. Uploading the Video

Open the web interface provided by Streamlit.

Upload the video file with improper audio (e.g., with ums, grammatical mistakes, etc.).


3. Processing

Once you upload the video, the following steps will take place automatically:

1. Transcription: The audio is extracted and sent to Google's Speech-to-Text API for transcription.


2. Grammatical Correction: The transcribed text is passed to OpenAI’s GPT-4 model to remove grammatical errors.


3. Synthesis: The corrected text is sent to Google’s Text-to-Speech API to generate a new audio file with AI-generated voice (Journey voice model).


4. Replacement: The new audio is synchronized with the original video, replacing the old audio track.



4. Downloading the Result

After processing, you can download the updated video file with the new AI-generated audio.



---

Credits

This project uses Google Cloud Speech-to-Text and Google Cloud Text-to-Speech APIs.

GPT-4 is powered by OpenAI (via Azure or OpenAI API).

Video and audio processing is handled by ffmpeg and moviepy.

