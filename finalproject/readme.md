# IDD Final Project
Hansen Guo

## Project Plan

Big idea: Music player with voice controls. The initial inspiration for this is the ipod nano music player. It is a music player that is small and minimalistic. You can control the whole music player by just using the touch screen. In my final project, I’ve decided to build a similar product with the raspberry pi. However, unlike the ipod nano, I am going to utilize voice controls instead of touch screens.

The user is going to be able to play and stop the music as well as to skip the current song. If time permits, I will also try to implement a shuffle function, where a random song in the current list is played instead.

The following shows the interactions drawn:

![Test Image 1](image0%20(17).jpg)

Timeline: In the following two weeks, the first week would probably be used to iterate through the prototype and designs as well as to try and get a functioning music player to work (without the voice controls). Then, in the second, I will reiterate some prototype and designs based on the user testing and feedback, as well as to integrate the voice controls into the device.

Parts needed: The parts needed should be the pi itself (along with the screen) as well as an audio input and output device (the webcam received in the class should be sufficient).

Risks/contingencies: As I have not coded a music player, there might be unseen difficulties and roadblocks that I will face along the way. Also, if I were to just use the webcam as my audio input and output device, I might face the issue of the inputs not being able to be heard clearly when the music is playing (the input command blending in with the music).

Fall-back plan: In case of the music player being an unsurpassable roadblock, I will end up building a music player prototype, where all the function except playing the music is present. The device, instead of playing the music, will use text-to-speech to say things like “song 1” to denote that a certain song is playing, and all other functionalities will still be present (pausing, resuming, skipping song, shuffle playlist etc).

## Documentation

Diagram drawing out the interaction:
![Test Image 1](image0%20(17).jpg)

Libraries Used: Pygames, gTTS, speechRecognition, pocketSphinx

When the program is ran, the first song will automatically start playing. The song that is currently playing will be displayed on the respberry pi screen. When the user presses a button, the program will briefly pause the song, and listen for the user's voice command. The program will use the speach recognition programs to recognize and interpret the user's command. If a valid command is received, the corresponding command will be executed; otherwise, the song will be unpaused (or nothing happens if the song is already paused before).

Currently valid inputs are: "Stop", to stop the song, and "Play" to unpause the song and continue playing it. The skip song input is implented but doesn't have the keyword that makes and have a higher success rate with reception (currently the command for skipping the song is "banana").

Below is a video of a user testing out the input:
https://drive.google.com/file/d/1FFHJS2IVKDPW0mBMpCMTVT52fFb9il10/view?usp=sharing

One feedback that was given was that sometimes the voice recognizer isn't accurate, and would sometimes misinterpret the command, and therefore not do what is intended. Because of that a few attempts was spent to solve this problem. First, I experimented using different words as the "command word". At first, I thought that the word "Pause" and "Resume" would be most fitting word for the device. But quickly, I changed it to "Stop" and "Play" because they are easier to say and recognize. Another attempt that I tried was to assign the commands a number and ask the user to say that (for example, assigning the stop function to "1" and the play function to "2"). This was because the calculator device I made in lab 3 was pretty successful, and I thought that the speech recognizer library was pretty good with recognizing numbers. However, with some testing with users, I found out that the accuracy was not greatly improved and was informed that this "code" is rather unintuitive. The last attempt that I did was try a different voice interpreter (using the google voice recognizer instead of the CMU pocket sphinx).

Then, I realized that maybe changing up the mic could help the reception. I pivotted the design of the product from using the usb mic that was distributed in class to a blue yeti mic of my own. This did result in a sizeable boost in consistency of the reception.

An updated video of the music player in action using the mic:
https://drive.google.com/file/d/1KjAgygYfir_h035MkpvHyx7rZHKno3tl/view?usp=sharing

## Video
Below is the final video of the music player in action:
https://drive.google.com/file/d/1KjAgygYfir_h035MkpvHyx7rZHKno3tl/view?usp=sharing

## Reflection of Process
The music player was far from perfect and still has lots of room for improvement, and lots of roadblocks could've been avoided with more forsight. For example, the audio reception issue could've been avoided and a lot of the time could've been saved if I had the insight to have used a better mic at the start. Also another forsight that would've been nice to have is to have tested the device in different environment. The room during the final presentation was much louder than my room where I did most of the testing. If I had the forsight or if I ever move forward with the project, I should've tested in more environment and taken these considerations into account. Other than that, I've enjoyed the process and had fun with the project.
