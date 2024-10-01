class TuringMachine:
    def __init__(self, tape, rules, initial_state, blank_symbol):
        self.tape = tape
        self.rules = rules
        self.state = initial_state
        self.head = 0
        self.blank_symbol = blank_symbol

    def step(self):
        current_symbol = self.tape[self.head]
        rule = self.rules.get((self.state, current_symbol))

        if rule:
            new_state, new_symbol, direction = rule
            self.tape[self.head] = new_symbol
            self.state = new_state
            
            if direction == 'R':
                self.head += 1
            elif direction == 'L':
                self.head -= 1
            
            # Expand the tape if the head moves out of current bounds
            if self.head < 0:
                self.tape.insert(0, self.blank_symbol)
                self.head = 0
            elif self.head >= len(self.tape):
                self.tape.append(self.blank_symbol)

    def run(self):
        while (self.state, self.tape[self.head]) in self.rules:
            self.step()
        return ''.join(self.tape).strip(self.blank_symbol)

# Definimos la cinta, las reglas y el estado inicial
tape = ['1', '1', '1', '0', '0']  # Ejemplo de cinta inicial
rules = {
    ('q0', '1'): ('q0', '1', 'R'),
    ('q0', '0'): ('q1', '0', 'R'),
    ('q1', '1'): ('q1', '1', 'R'),
    ('q1', '0'): ('q1', '0', 'R'),
    ('q1', ' '): ('q2', ' ', 'L'),  # Estado de aceptación
}
initial_state = 'q0'
blank_symbol = ' '

# Creamos y ejecutamos la máquina de Turing
tm = TuringMachine(tape, rules, initial_state, blank_symbol)
result = tm.run()

print(f'Tape final: {result}')
