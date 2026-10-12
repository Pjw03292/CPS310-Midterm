
import json
from storage import StateStorage


class JSONStorage(StateStorage):

    def __init__(self, filename):
        self.filename = filename

    def save_state(self, state):
        with open(self.filename, "w") as file:
            json.dump(state, file, indent=4)

        print("Game saved to JSON file!")

    def load_state(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return None
