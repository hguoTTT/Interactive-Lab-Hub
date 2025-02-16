# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Math tutor bot. The math tutor bot aims to teach first grade children how to do simple additions and subtractions. It is meant to be acted as an alternative to paper problem sets and test the children in a more conversational way so that it he/she can feel more engaged in learning math. Also, it can come up with endless questions, so the children can have as much practice as he/she wants. The bot would first ask the children a simple addition or subtraction problem through text to speech, and would then wait for a respoce. If the children got the question right, the bot will congratulate the children, and move on. If the children got the quesiton wrong, the bot will prompt the children to try again.

![Test Image 1](image0%20(9).jpg)

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

A video of the interaction acted out:
https://drive.google.com/file/d/15tbfG_PGSsya5jZ0Mlh0nTfWD82iuLQ3/view?usp=sharing

One thing that I have noticed when acting the scene out is that it might have been a good idea to repeat the question when the user gets it right. Looking at the recording, I realized that it took me a second to remember what the question originally was when I was prompted to try again. Therefore, repeating the question would greatly help the user refresh their memories.

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

As stated earlier, through testing the interaction, I've realized that it might be helpful that I repeat the question, when the user gets the answer wrong. This is because repeating the question helps the user refresh their memories and remember what the question was.

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

Maybe aside from speech, it might be helpful to provide the users with a visual aid of what the question is, and what the user should be doing.

4. Make a new storyboard, diagram and/or script based on these reflections.

![Test Image 1](image0%20(11).jpg)

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

Libraries Used:
gTTS, word2number, speechRecognition, pocketSphinx

When prototype.py is ran, the script will generate a random simple math quesiton. It is outputed through the text2speech functions, and broadcasted so that the user hears it. The system then waits for the user to provide a resonse. It takes in the response through the voice recognition and interprets with the pocketSphinx library. The reponse it then converted with a word2number library and compared to the answer. If the user answers the question correct, they are congratulated and a new question is generated. If they got the answer wrong, they are prompted to try again, the and the system will repeat the question.

*Include videos or screencaptures of both the system and the controller.*

Video of the Interaction: https://drive.google.com/file/d/1_uwIvZcGtqb52hsZbI9r3aZ0g35GUCAj/view?usp=sharing

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
The system worked well in the sense that it is able to generate endless questions if needed to be. One thing that didn't work well is that the system is not so good at recepting a negative answer, so it has to be programmed explicitly so that the answer would always be positive (making sure the first number is always bigger than the second number).

### What worked well about the controller and what didn't?
One thing that works well is that since the answer the user imputs are usually fairly simple, the recpetion has been decent and fairly accurate. One thing that didn't work so well is that the wait time can be hard to tune. There need to be enough time given for the user to react, but sometimes there is a slight wait if we make the reception time too long.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
Designing an autonomous version of the system can be hard because it is hard to always know what the persion would do or say. In my device's instance, although the answer is usually fairly straight forward, and I can expect the user to give me a somewhat reasonable response, it is still hard to determine how much time to give user to answer the question. Since it is hard for the machine to recognize when the user is done answering, I have to leave the reception on for the whole duration. Therefore, it is hard to balance how long for the reception to be.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
A part from the sound, other modes of possible interactions includes having a visual. It makes sense for the user to, apart from hearing the math question, also have an alternative way of retrieving the information (displaying the qeustion on some sort of screen).

