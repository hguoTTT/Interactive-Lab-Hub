from gtts import gTTS
import os
  
correctText = 'Congratulations, you are correct.'
incorrectText = 'Try again.'
  
language = 'en'
correct = gTTS(text=correctText, lang=language, slow=False)
inccorect = gTTS(text=incorrectText, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named
correct.save("correct.mp3")
incorrect.save("incorrect.mp3")
  
# Playing the converted file
os.system("mpg321 correct.mp3")
