class MealyState:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, input_symbol, next_state, output_symbol):
        self.transitions[input_symbol] = (next_state, output_symbol)

    def get_transition(self, input_symbol):
        return self.transitions.get(input_symbol, (None, None))

class MealyMachine:
    def __init__(self):
        self.states = {}
        self.initial_state = None

    def add_state(self, state):
        self.states[state.name] = state
        if self.initial_state is None:
            self.initial_state = state

    def set_initial_state(self, state_name):
        self.initial_state = self.states.get(state_name)

    def process_input(self, input_sequence):
        current_state = self.initial_state
        outputs = []

        for symbol in input_sequence:
            if current_state is None:
                raise Exception("No transition defined for this input symbol.")

            next_state, output_symbol = current_state.get_transition(symbol)
            if next_state is None:
                raise Exception(f"No transition defined for symbol '{symbol}' in state '{current_state.name}'.")

            outputs.append(output_symbol)
            current_state = next_state

        return outputs

s1 = MealyState("S1")
s2 = MealyState("S2")
s3 = MealyState("S3")

s1.add_transition("a", s2, "x")
s1.add_transition("b", s3, "y")
s2.add_transition("a", s1, "z")
s2.add_transition("b", s3, "w")
s3.add_transition("a", s3, "u")
s3.add_transition("b", s1, "v")


machine = MealyMachine()
machine.add_state(s1)
machine.add_state(s2)
machine.add_state(s3)


machine.set_initial_state("S1")

input_sequence = ["a", "b", "a", "a", "b"]
output_sequence = machine.process_input(input_sequence)
print("Output sequence:", output_sequence)
