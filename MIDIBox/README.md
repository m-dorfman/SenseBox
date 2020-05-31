# MIDIBox

## MIDIBox is a midi utility for use with RaspberryPi and the MFRC522 rfid module. It simply takes a fixed set of value from either a file or a self generated list and outputs them as a JSON message. The messages can be be sent to a virtual midi instrument for playback. 

---

## Requirements: 
- Python 3, 3.6 recommended 
- check the requirements.txt file for library requirements, built with pip
- needed clone of sultan can be found at https://github.com/aeroxis/sultan
- ``` git clone https://github.com/aeroxis/sultan.git ```

---

## Using:
 can simply call the file as ``` ./rfid-read.py ```
 this will now send out json messages using midi data
### 
- to use with preset values simply create a list in the midi_container.txt files, calues should not exceed 88
### 
- you can also read back values of rfid cards to cheack for associations by calling the object: ``` ./rfid-read.py UID_Builder.serial_uid_builder() ```. this will return a json object
- this can also be called externally to load values into a message and send it off, ie this can act like a simple reader that sends a json message
### 
- to play some sounds the ``` midi_play.py ``` script is needed. running this will launch into VMPK, a simple midi keyboard utility, we take advantage of it via rfid keys.
### 
