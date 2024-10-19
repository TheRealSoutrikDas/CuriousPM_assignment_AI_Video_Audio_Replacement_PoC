import openai
from config import AZURE_API_KEY, AZURE_ENDPOINT

def correct_transcription(transcription):
    openai.api_key = AZURE_API_KEY

    response = openai.Completion.create(
        engine="gpt-4o",
        prompt=f"Correct the following text:\n\n{transcription}",
        temperature=0.7,
        max_tokens=500
    )

    corrected_text = response.choices[0].text.strip()
    return corrected_text