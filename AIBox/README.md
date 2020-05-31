# AIBox

## AIBox is a version of SenseBox software that takes advantage of SenseBox's midi functionality by leveraging TensorFlow via Magenta(https://github.com/tensorflow/magenta).
## SenseBox recieves midi input via RFID tags which have an associated midi note in a buffer. Once the buffer has either fully filled or when a long enough period of time elapses, a model takes the input buffer and responds to it(values of buffer size and time can be adjusted). The response depends on the model used and usage is referenced below.

---

## Requirements:
### Magenta should be installed to run. Use the development instructions, https://github.com/tensorflow/magenta, found on their page or use the utility that's in this folder: ``` ./magentamake.sh -i ```
### if running the above utility then no need tto clone but otherwise the project should be cloned: ``` git clone https://github.com/tensorflow/magenta.git ```
### models also need to be obtained, the melody recurrent network was used which can be downloaded from the following page: https://github.com/tensorflow/magenta/tree/master/magenta/models/melody_rnn; these should be loaded into this directory

---

## Using:
### To run ``` ./aiplay.py ``` and begin by scanning rfid tags.