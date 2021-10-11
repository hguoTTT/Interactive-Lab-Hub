from gtts import gTTS
from word2number import w2n
import speech_recognition as sr
import os
import random
  
correctText = 'Congratulations, you are correct.'
incorrectText = 'Try again.'
  
language = 'en'
correct = gTTS(text=correctText, lang=language, slow=False)
incorrect = gTTS(text=incorrectText, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named
correct.save("correct.mp3")
incorrect.save("incorrect.mp3")
  
# Playing the converted file
#os.system("mplayer correct.mp3")

#Set up speech recognition
r = sr.Recognizer()

def main():
  a = random.randint(5,9)
  b = random.randint(0,5)
  c = random.randint(0,1)
  d = 0
  if c == 0:
    questionText = "What is " + str(a) + " minus " + str(b)
    answer = a-b
  else:
    questionText = "What is " + str(a) + " plus " + str(b)
    answer = a+b
  while true:
    question = gTTS(text=questionText, lang=language, slow=False)
    question.save("question.mp3")
    os.system("mplayer question.mp3")
    with sr.Microphone() as source:
      audio = r.listen(source)
    response = r.recognize_sphinx(audio)
    responseInt = w2n.word_to_num(response)
    if reponseInt == answer:
      os.system("mplayer correct.mp3")
      a = random.randint(5,9)
      b = random.randint(0,5)
      c = random.randint(0,1)
      d = 0
      if c == 0:
        questionText = "What is " + str(a) + " minus " + str(b)
        answer = a-b
      else:
        questionText = "What is " + str(a) + " plus " + str(b)
        answer = a+b
    else:
      os.system("mplayer incorrect.mp3")

main()
