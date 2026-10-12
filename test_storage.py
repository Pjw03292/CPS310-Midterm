
import unittest
import tempfile
import os

from simulation import Simulation
from memory_storage import MemoryStorage
from json_storage import JSONStorage


class TestStorage(unittest.TestCase):

    def test_memory_storage(self):
        storage = MemoryStorage()
        game = Simulation(storage)

        game.run_round()

        saved_state = storage.load_state()

        self.assertEqual(saved_state, game.state)
        self.assertEqual(saved_state["round"], 1)

    def test_json_storage(self):
        with tempfile.TemporaryDirectory() as folder:
            filename = os.path.join(folder, "test_game.json")
            storage = JSONStorage(filename)
            game = Simulation(storage)

            game.run_round()

            saved_state = storage.load_state()

            self.assertEqual(saved_state, game.state)
            self.assertEqual(saved_state["round"], 1)

    def test_both_storage_methods_match(self):
        memory = MemoryStorage()

        with tempfile.TemporaryDirectory() as folder:
            filename = os.path.join(folder, "test_game.json")
            json_storage = JSONStorage(filename)

            game1 = Simulation(memory)
            game2 = Simulation(json_storage)

            for i in range(3):
                game1.run_round()
                game2.run_round()

            self.assertEqual(
                memory.load_state(),
                json_storage.load_state()
            )


if __name__ == "__main__":
    unittest.main()
