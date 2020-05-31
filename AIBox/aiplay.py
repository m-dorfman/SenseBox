(require = ../MIDIbox/) 
import midi-play
import rfid-read
import mido
import sultan

"""
midi channels:

        | vmpkOUT   |   sBoxOUT   |  magenOUT
--------|-----------|-------------|-------------
sBoxIN  |    no     |    no       |     no
--------|-----------|-------------|-------------
vmpkIN  |    yes    |    no       |     yes
--------|-----------|-------------|-------------
magenIN |    no     |    yes      |     no

"""

magenta_port_in = mido.open_output(12)
magenta_port_out = mido.open_input(10)

command =" #this needs to be adjusted w/ proper midi hookups
BUNDLE_PATH=./lookback_rnn.mag
CONFIG=lookback_rnn
melody_rnn_generate \
--config=${CONFIG} \
--bundle_file=${BUNDLE_PATH} \
--output_dir=/tmp/melody_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
--primer_melody="[60]"
"
s = Sultan()

s.user(command).run()