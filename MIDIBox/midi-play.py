import subprocess
from sultan.api import Sultan #https://github.com/aeroxis/sultan
from ./rfid-read import MIDI_Construct
import bidict

class Instrument:
    def __init__(self):
        self.midi_hookup()

    def midi_hookup():
        """
        midi channels:
        
                | vmpkIN   |   vmpkOUT
        --------|----------|------------
        sBoxIN  |    no    |   no
        --------|----------|-------------
        sBoxOUT |    yes   |   no

        """
        sBox_outport = mido.open_output(10)
        vpmk_inport = mido.open_input(10)

        runner = Sultan()
        runner.vpmk("-im 10").run() # launch vmpk on port 10


class Player:
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def midi_to_instrument(input, output): #currently hardcode, should update
        main_ = MIDI_Construct()
        post_set = main_.midi_iter
        final_create = tag_note_loader(post_set)
        def send(midi_container):
            final = json.loads(midi_container)
            return final
        return send(final_create)


if __name__ == "__main__":
    instrument = Instrument() #launches ports and instrument
    player = Player(10,10)
    for i in (note = player.midi_to_instrument):
        the_note = note(i)
        mido.msg(10, the_note)