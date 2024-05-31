import openai


file = "/Users/zoeakpan/Desktop/personal projects/Hello [sound effect].mp3"

#easy to change file
def transcribing(file):
# no way the api key should be shared but i dont want to create an env folder
    openai.api_key = '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'
    audio = open(file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio)

transcribing(file)
