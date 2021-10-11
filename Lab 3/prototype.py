from gtts import gTTS
import os
  
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

def main()
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
  question = gTTS(text=questionText, lang=language, slow=False)
  qeustion.save("question.mp3")
  os.system("mplayer question.mp3")

main()
