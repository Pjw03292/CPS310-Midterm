
from storage import StateStorage


class MemoryStorage(StateStorage):

    def __init__(self):
        self.state = None

    def save_state(self, state):
        self.state = state.copy()
        print("Game saved to memory!")

    def load_state(self):
        if self.state is not None:
            return self.state.copy()
        return None
