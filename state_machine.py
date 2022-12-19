from state import State


class StateMachine:
    def __init__(self, start_state: State, end_state: State):
        self.start_state = start_state
        self.end_state = end_state
        self.current_state = self.start_state

    def test(self, input_str):
        for character in input_str:
            self.current_state = self.current_state.next_state(character)
            if self.current_state is None:
                print()
                raise ValueError(f"Такой комбинации нету")
            print(self.current_state.message, end='')

        return self.current_state == self.end_state
