# CPS 310 Midterm - Zombie Game Simulation
# Patrick Williams
## About the Project

For this midterm, I made a simple zombie simulation using Python. The game starts with 5 humans and 3 zombies. Each round, the zombies attack humans and take away 20 health. The program also keeps track of the round number, location, weather, and time.

The main goal of this project was to make the simulation work with different ways of saving information without having to change the game itself.

## How It Works

I made a few different Python files to separate the game from the storage.

- `simulation.py` runs the game and handles the zombie attacks.
- `storage.py` sets up the basic rules for saving and loading information.
- `memory_storage.py` saves the game information in memory.
- `json_storage.py` saves the information in a JSON file.
- `main.py` runs the simulation using both storage methods.

Both storage methods use the same save and load functions. This lets the game switch between them without changing how the simulation works.

## Why I Designed It This Way

I separated the storage from the simulation so that changing how the game saves information would not affect the game itself.

I used classes and inheritance to make both storage methods follow the same setup. The simulation uses whichever storage method is given to it.

This makes it easier to add another storage method in the future without rewriting the whole program.

## Testing

I made a `test_storage.py` file to check that everything worked correctly.

I tested saving and loading with memory storage, saving and loading with JSON storage, and whether both methods gave the same results.

All 3 tests passed.

## How to Run

To run the simulation:

```bash
py main.py
```

To run the tests:

```bash
py -m unittest test_storage.py
```

## Conclusion

This project helped me understand how to use classes in Python and how to keep different parts of a program separate. I was able to make two storage methods work with the same zombie simulation without changing the simulation code.
