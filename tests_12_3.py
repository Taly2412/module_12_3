import unittest
from runner import Runner
import runner_and_tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        self.runner_1 = Runner('1')
        for _ in range(10):
            self.runner_1.walk()

        self.assertEqual(self.runner_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        self.runner_2 = Runner('2')
        for _ in range(10):
            self.runner_2.run()
        self.assertEqual(self.runner_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.runner_3 = Runner('3')
        self.runner_4 = Runner('4')
        for _ in range(10):
            self.runner_3.run()
            self.runner_4.walk()
        self.assertNotEqual(self.runner_3.distance, self.runner_4.distance)



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results, sep='\n')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        _tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.all_results.append(_tournament.start())
        index = len(self.all_results[-1])

        self.assertTrue(self.all_results[-1][index] == self.runner3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        _tournament = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.all_results.append(_tournament.start())
        index = len(self.all_results[-1])

        self.assertTrue(self.all_results[-1][index] == self.runner3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        _tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results.append(_tournament.start())
        index = len(self.all_results[-1])

        self.assertTrue(self.all_results[-1][index] == self.runner3.name)




if __name__ == "__main__":
    unittest.main()
