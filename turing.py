class TuringMachine:
    def __init__(self, file_path, tape_file):
        self.states_dict = self.load_states_from_file(file_path)
        self.state = "start"
        self.head_position = 1
        self.tape = self.load_tape(tape_file)

    def load_states_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        states = {}
        for line in lines:
            state, value = line.split(':')
            states[state] = eval(value)
        return states

    def load_tape(self, tape_file):
        with open(tape_file, "r") as file:
            tape = list(file.read())
            tape.insert(0, " ")
            tape.append(" ")
        return tape

    def run(self):
        while self.state != 'acc' and self.state != 'false':
            self.state, self.head_position = self.process_state(self.state, self.head_position)
        print(self.state)

    def process_state(self, state, head_position):
        for value in self.states_dict[state]:
            for znak in value[0]:
                if znak == self.tape[head_position]:
                    if value[1] != "": #zmiana znaku, jeśli w odczytanym stanie należy zmienić znak na taśmie
                        self.tape[head_position] = value[1]
                    if value[2] == 'L':  #L-left - głowica w Lewo, czyli -1
                        head_position -= 1
                    elif value[2] == 'R': #R-right - głowica w Prawo, czyli +1
                        head_position += 1
                    if value[3] != "":
                        state = value[3]  #zmiana stanu, jeśli w odczytanym stanie należy zmienić stan 
                    return state, head_position

if __name__ == "__main__":
    file_path = 'states.txt'
    tape_file = 'tape.txt'

    turing_machine = TuringMachine(file_path, tape_file)
    turing_machine.run()