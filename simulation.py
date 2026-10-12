
class Simulation:

    def __init__(self, storage):
        self.storage = storage

        self.state = {
            "humans": [
                {"name": "Human 1", "health": 100},
                {"name": "Human 2", "health": 100},
                {"name": "Human 3", "health": 100},
                {"name": "Human 4", "health": 100},
                {"name": "Human 5", "health": 100}
            ],
            "zombies": 3,
            "round": 0,
            "environment": {
                "location": "Abandoned City",
                "weather": "Foggy",
                "time": "Night"
            }
        }

    def load_game(self):
        saved_state = self.storage.load_state()

        if saved_state is not None:
            self.state = saved_state
            print("Previous game loaded!")
        else:
            print("No saved game found.")

    def run_round(self):
        self.state["round"] += 1

        print("\nRound", self.state["round"])

        # Each zombie attacks the first living human
        for zombie in range(self.state["zombies"]):

            for human in self.state["humans"]:
                if human["health"] > 0:
                    human["health"] -= 20
                    print(human["name"], "was attacked!")
                    break

        self.storage.save_state(self.state)

    def show_state(self):
        print("\nCurrent Game State:")

        for human in self.state["humans"]:
            print(human["name"], "- Health:", human["health"])

        print("Zombies:", self.state["zombies"])
        print("Round:", self.state["round"])

        print("Location:", self.state["environment"]["location"])
        print("Weather:", self.state["environment"]["weather"])
        print("Time:", self.state["environment"]["time"])
