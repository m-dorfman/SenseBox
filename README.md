# SenseBox
---

## SenseBox is an RFID based modular system that can associate a sound to any given tag. ie, scan a tag, make a sound. 

## SenseBox can be reproduced by anyone with access to a 3d printer, soldering iron and the internt. All components can be ordered from the Adafruit website and costs approximately $35usd. 

---

## What is this page?
### This page includes some side projects to make SenseBox a more programtically interesting device. Currently it include a basic utility to turn the device into a MIDI capable system where rfid tags can have notes associated to them. The second part is to allow SenseBox to take advantage of neural network models by way of TensorFlow. We employ Magenta to allow us to input midi and recieve midi as a response from the neural model. 

---

### Some dependencies:
#### bidict python
#### mido python
#### jackclient python
#### check individual requirements in subdirectories

---

### Note for setup: this project depends on the use of Ubuntu. Any version of a Debian flavor linux can be used but the project was developed with Ubunutu as the OS(Raspbian did not work).