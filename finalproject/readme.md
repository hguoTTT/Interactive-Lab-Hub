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

When the program is ran, the first song will automatically start playing. When the user presses a button, the program will briefly pause the song, and listen for the user's voice command. The program will use the speach recognition programs to recognize and interpret the user's command. If a valid command is received, the corresponding command will be executed; otherwise, the song will be unpaused (or nothing happens if the song is already paused before).

Currently valid inputs are: "Stop", to stop the song, and "Play" to unpause the song and continue playing it.

## Video
Below is a video of the music player in action:
https://drive.google.com/file/d/1JC0UDHwOXK79AA28ndHGVjyrjW76YM35/view?usp=sharing