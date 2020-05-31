import time
import RPi.GPIO as GPIO
import MFRC522
import bidict
import thread
import json
import mido
import importlib

# create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
global json_uid = None

class UID_Builder: #in the case of uid checking, called with flag
    def serial_uid_builder():
        lock = thread.allocate_lock()
        while True:
            try:
                n = 0
                while True:
                # Scan for cards
                    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
                # Get the UID of the card
                    (status,uid) = MIFAREReader.MFRC522_Anticoll()
                # If we have the UID, continue
                    if status == MIFAREReader.MI_OK:
                        json_uid[n] = str(uid).split()
                        time.sleep(2)
                break
        finally:
        return json.loads(json_uid)
        GPIO.cleanup()

class MIDI_Construct:
    def tag_note_loader(midis):
        lock = thread.allocate_lock()
        thread.start_new_thread(self)
        reader = MFRC522.SimpleMFRC522()
        midis = midi_iter()
        if value_builder() == True:
            for i in midis:
                vals = value_builder
                tags[vals[i]] = reader.write('')
        for i in midis:
            tags[i.note] = reader.write('')
        return tags
    
    def self.midi_iter(): # this is a cheap computation so i do it regardles of preset existence
        notes = []
        for n in [48:84]: # we can only use midi encoded values from 48 on
            if n < 84:
                number = n + (n%2) - (n%12)
                notes[n] = mido.Message('note_on', note=number)
            else:
                break
        return notes
    
    def self.value_builder(): # used to build the value set from external file
        try:
            importlib.import_file(midi_container.txt)
            return list(importlib.import_file(midi_container.txt)), True
        else:
            return False
