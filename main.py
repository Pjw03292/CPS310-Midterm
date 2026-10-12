
from simulation import Simulation
from memory_storage import MemoryStorage
from json_storage import JSONStorage


def main():

    print("=== MEMORY STORAGE ===")

    memory = MemoryStorage()
    game1 = Simulation(memory)

    for i in range(3):
        game1.run_round()

    game1.show_state()

    print("\n=== JSON STORAGE ===")

    json_storage = JSONStorage("game_state.json")
    game2 = Simulation(json_storage)

    for i in range(3):
        game2.run_round()

    game2.show_state()

    print("\n=== LOADING SAVED GAME ===")

    loaded_game = Simulation(JSONStorage("game_state.json"))
    loaded_game.load_game()
    loaded_game.show_state()


if __name__ == "__main__":
    main()
