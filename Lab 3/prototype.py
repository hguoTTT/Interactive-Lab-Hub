from gtts import gTTS
import os
  
correctText = 'Congratulations, you are correct.'
  
language = 'en'
myobj = gTTS(text=correctText, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
myobj.save("correct.mp3")
  
# Playing the converted file
os.system("mpg321 correct.mp3")
