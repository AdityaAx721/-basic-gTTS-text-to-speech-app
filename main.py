# -*- coding: utf-8 -*-
from gtts import gTTS
import os
##create the folder for store voice 
os.makedirs("output",exist_ok=True)

text = "hello Boss, friday at your service"
#text="क्रिस्टियानो रोनाल्डो डॉस सैंटोस अवेइरो, जिन्हें क्रिस्टियानो रोनाल्डो के नाम से जाना जाता है। उनका शुमार दुनिया के सबसे महान फुटबॉल खिलाड़ियों में से एक में होता है। क्रिस्टियानो रोनाल्डो का जन्म 5 फरवरी 1985 को मदीरा, पुर्तगाल में हुआ था। रोनाल्डो एक गरीब परिवार से थे और अपने चार भाई-बहनों में सबसे छोटे थे।"
tts=gTTS(text=text,lang="en")

file_path= "output/output_en.mp3"
tts.save(file_path)

print("Audio generated sucessfully :",file_path)
