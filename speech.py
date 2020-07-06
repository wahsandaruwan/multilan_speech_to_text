import speech_recognition as sr

# Create recognizer object
recog = sr.Recognizer()

# Use microphone to get the voice
with sr.Microphone() as source:
    print("Say Something : ")
    audio = recog.listen(source)
    print("Done!")

# Define the speaking language
text = recog.recognize_google(audio, language = 'si-LK')

# Print the what said in partcular language
print(text)

# Print the vocie in english
print(recog.recognize_google(audio, language = 'en-US'))