# Voice-Command-AI-Bot-Jarvis
Overview
The Voice Command AI Bot, also known as "Jarvis," is a simple yet powerful voice assistant that interacts with users through speech. It can perform various tasks such as searching Wikipedia, opening popular websites like YouTube and Google, telling the current time, and launching desktop applications. The bot responds based on voice commands provided by the user and executes tasks automatically.

Features
Voice Interaction: The bot listens to user input and responds verbally.
Dynamic Greetings: It greets users based on the time of day (morning, afternoon, or evening).
Wikipedia Search: The bot can search Wikipedia and provide concise summaries of topics.
Web Navigation: It can open websites such as YouTube, Google, and others based on voice commands.
Application Launcher: You can launch various applications such as VS Code, Atom, or Illustrator directly from your voice commands.
Time Inquiry: It can tell the current time when asked.
Custom Extensions: Easily extend the bot by adding additional tasks or commands.
Technologies Used
Python: The core programming language used to implement the bot.
pyttsx3: A text-to-speech conversion library to allow the bot to speak.
speech_recognition: For recognizing and processing voice input.
wikipedia: For fetching information from Wikipedia.
webbrowser: To open websites in the default web browser.
os: For launching local applications.
Setup Instructions
Prerequisites
Ensure you have Python installed on your system. You will also need to install the following Python libraries:

pyttsx3
SpeechRecognition
wikipedia

Example Commands
"Open YouTube"
"Search Wikipedia for Python programming"
"What is the time?"
"Open VS Code"
"Play anime"
Customization
You can modify the paths for applications such as VS Code, Atom, and Adobe Illustrator within the script.
Add more commands to extend functionality by editing the elif block in the main loop.
Future Enhancements
Add voice recognition to support multiple languages.
Integrate with more web APIs for advanced features.
Implement machine learning for personalized responses.
License
This project is open-source. Feel free to modify and use it in your projects!

Contribution
If you find any bugs or would like to add more features, feel free to fork this repository and submit a pull request.

