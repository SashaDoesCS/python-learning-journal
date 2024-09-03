import random


class Pokemon:
    def __init__(self, name, p_type, hp, attack, defense, moves, crit_chance):
        self.name = name
        self.p_type = p_type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = moves  # List of tuples (move_name, move_power)
        self.crit_chance = crit_chance  # Critical hit chance (0.0 to 1.0)

    def use_move(self, move_name, other_pokemon):
        if self.hp <= 0:
            print(f"{self.name} is knocked out and cannot attack.")
            return False

        move = next((m for m in self.moves if m[0].lower() == move_name.lower()), None)
        if not move:
            print(f"{self.name} cannot use {move_name}.")
            return False

        move_name, move_power = move
        print(f"{self.name} uses {move_name}!")

        # Check for critical hit
        is_crit = random.random() < self.crit_chance
        crit_multiplier = 2 if is_crit else 1

        damage = (move_power + self.attack - other_pokemon.defense) * crit_multiplier
        if damage < 0:
            damage = 0

        if is_crit:
            print("It's a critical hit!")

        other_pokemon.hp -= damage
        print(f"{other_pokemon.name} takes {damage} damage and has {other_pokemon.hp} HP left.")

        if other_pokemon.hp <= 0:
            other_pokemon.hp = 0
            print(f"{other_pokemon.name} is knocked out!")
            return True

        return False


def battle(player_pokemon, opponent_pokemon):
    print(f"A wild {opponent_pokemon.name} appears!")
    while player_pokemon.hp > 0 and opponent_pokemon.hp > 0:
        print("\nYour moves: ", ", ".join([move[0] for move in player_pokemon.moves]))
        player_move = input("Choose your move: ").strip()

        # Player's turn
        if player_pokemon.use_move(player_move, opponent_pokemon):
            print(f"You defeated {opponent_pokemon.name}!")
            break

        # Opponent's turn (random move)
        if opponent_pokemon.hp > 0:
            opponent_move = random.choice(opponent_pokemon.moves)[0]
            if opponent_pokemon.use_move(opponent_move, player_pokemon):
                print(f"{opponent_pokemon.name} defeated your {player_pokemon.name}!")
                break

    if player_pokemon.hp > 0:
        print(f"\nYou won! {player_pokemon.name} is still standing with {player_pokemon.hp} HP left.")
    else:
        print(f"\nYou lost! {player_pokemon.name} is knocked out.")


# Example usage:
pikachu = Pokemon(
    "Pikachu", "Electric", 35, 10, 5,
    [("Thunder Shock", 10), ("Quick Attack", 7), ("Electro Ball", 8), ("Iron Tail", 9)],
    crit_chance=0.2  # 20% chance for a critical hit
)

charmander = Pokemon(
    "Charmander", "Fire", 39, 8, 4,
    [("Ember", 8), ("Scratch", 6), ("Flamethrower", 12), ("Fire Spin", 10)],
    crit_chance=0.15  # 15% chance for a critical hit
)

battle(pikachu, charmander)
