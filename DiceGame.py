import random


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        self._value = random.randint(1, 6)
        return self._value


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        self._die.roll()


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("=============================")
        print("🎲 Welcome to Roll the Dice!")
        print("=============================")

        while True:
            self._play_round()
            game_over = self._check_game_over()
            if game_over:
                break

    def _play_round(self):
        self._print_round_welcome()

        self._roll_the_dice()

        self._show_dice(self._player.die.value, self._computer.die.value)

        if self._player.die.value > self._computer.die.value:
            print("You won the round!")
            self._update_counters(winner=self._player, loser=self._computer)
        elif self._computer.die.value > self._player.die.value:
            print("The computer won this round. Try again.")
            self._update_counters(winner=self._computer, loser=self._player)
        else:
            print("It's a tie!")

        self._show_counters()

    def _print_round_welcome(self):
        print("\n--------- New Round ---------")
        input("🎲 Press any key to roll the dice. 🎲")

    def _show_dice(self, player_value, computer_value):
        print(f"Your die: {player_value}")
        print(f"Computer die: {computer_value}\n")

    def _update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def _show_counters(self):
        print(f"\nYour counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")

    def _check_game_over(self):
        if self._player.counter == 0:
            self._show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self._show_game_over(self._computer)
            return True
        else:
            return False

    def _show_game_over(self, winner):
        print("\n=================")
        print("G A M E O V E R")
        print("===================")
        if winner.is_computer:
            print("The computer won the game. Sorry...")
        else:
            print("You won the game! Congratulations.")
        print("==================================")

    def _roll_the_dice(self):
        self._player.roll_die()
        self._computer.roll_die()


player_die = Die()
computer_die = Die()

my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

game.play()
