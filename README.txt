Hello,

Welcome to my thesis project. 

The project that definitely caused a lot of stress, sweat and even tears - but at the end, I can definitely say it was worth it and I would do it again.

Thesis Background:
2023, Technological Unversity of Dublin - Blanchardstown Campus
Digital Forensics & Cyber Security (Hons) 

For our thesis guidelines we were asked to solve a problem, the lecturers were stating that our projects cannot be based on just 'hypothetical situations' but rather more of real-life scenarios that we are currently dealing with in the world cyber security and how could we solve some of these problems.
Bottom line - Through this thesis we must solve a problem.

Thesis idea:
My project was based on a keylogger detection application. As we know no system is bullet-proof from malicious attacks and applications. I have personally dealt with keylogger attacks before and decided that this would be a perfect time to use my knowledge to perform attacks on myself and show the base results after using some defense techniques.

I have decided to develop a keylogger detection application using Python, I have used the Python keylogger codes of other cyber security contributors such as David Bombal, while testing with their snippets of code I started to look for ways to bypass anti-viruses, I have failed with even some trial version anti-viruses but upon further testing, I have discovered that a freshly converted .exe keylogger can run and be completely masked from the active Microsoft Defender.

Files:
Please note! Some of these files contain snippets of keylogger code, so please download them at your own risk - your anti-virus may flag some of these files as trojan malwares, so again - please use at own risk!

- Keylogger Detector
This is the main folder containing Python code that was used to develop a keylogger detector using the most basic methods, methods involving: taking all of the MD5 hashes from every actively running task in your Windows machine and cross checking them with VirusTotal using the VirusTotal API key, which if a positive result for a keylogger or spyware came back - our application would warn us and remove the suspected keylogger.

- Python Keylogger
Basic keylogger code snippet that was borrowed from David Bombal's website.

- C++ Converted Keylogger
This code did not make it into the final cut of the assignment but I thought it would still be a great idea to include the elements used throught the project for testing purposes, a Python keylogger was convereted into a C++ keylogger which would use the exact same keylogging methods although detection rate was interesting to find, the detection rate did not differ that much but Python keylogger was more detectable than C++ keylogger.

- TXT Uploader to DropBox
VirusTotal wasn't the only contributor to this project using the API key, DropBox also came in handy to showcase the methods that would be used by a threat actor to extort the keylogger information from the user machines and send it back to their own green area. In this case; since our keylogger was saving all of the keystrokes with timestamps in a .txt document, this TXT Uploader would take that .txt file that is constantly updating while the keylogger is running and upload that to the DropBox every 30/60 seconds (editing tyhe time in the code however you like)

- Virus Downloader
Of course we cannot showcase our attack and defence methods from the middle, I wanted to make sure that I have it showcased from start to finish as in a real-life scenario. Virus Downloader was disguised as an 'esset installer' which would realistically, install the keylogger and the .vbs script file which would run the keylogger in the background without the user noticing a difference in the GUI as well as downloading and shadow running the uploader which will upload the updated .txt file with logged keystrokes and timestamps. 

Documents:
Of course, for a successful thesis you need to do two main parts which is writing and then testing (or wise-versa) 

- code_appendice.pdf 
This .pdf document contains the links of all borrowed code.

- thesis_document.pdf
The main document which contains a total of +18,000 words in the whole document, the document contains the important parts which are: Introduction, Literature Review, Methodology, Implementation & Testing and finally Analysis of Results.
This document covers every single part of the project in detail.

- thesis_presentation.pptx
Of course, the project would not be patent by me if I did not do a presentation on it, not to just 2 lecturers but a class containing 28 students. The PowerPoint will contain 2 videos showcasing the infection methods of the keylogger and it's execution with verification of running Microsoft Defender as well as the keylogger detector in action.


Have a nice surf! : )
