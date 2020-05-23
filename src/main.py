import pygame
from pygame.locals import *
from models.Battle import *
from models.Pokemon import *

# First, define pokemon with its stats
pokemon1 = Pokemon("Bulbasaur", 100, 11, 3)
pokemon2 = Pokemon("Charmander", 100, 9, None)

pokemon1.current_hp = 45
pokemon2.current_hp = 39

# Stats
pokemon1.baseStats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}

pokemon1.ev = {
    HP: 0,
    ATTACK: 0,
    DEFENSE: 0,
    SPATTACK: 0,
    SPDEFENSE: 0,
    SPEED: 0
}

pokemon1.iv = {
    HP: 21,
    ATTACK: 21,
    DEFENSE: 21,
    SPATTACK: 21,
    SPDEFENSE: 21,
    SPEED: 21
}

pokemon1.compute_stats()

pokemon2.baseStats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}

pokemon2.ev = {
    HP: 0,
    ATTACK: 0,
    DEFENSE: 0,
    SPATTACK: 0,
    SPDEFENSE: 0,
    SPEED: 0
}

pokemon2.iv = {
    HP: 21,
    ATTACK: 21,
    DEFENSE: 21,
    SPATTACK: 21,
    SPDEFENSE: 21,
    SPEED: 21
}

pokemon2.compute_stats()

# Attacks
pokemon1.attacks = [Attack("Vine Whip", 11, PHYSICAL, 10, 10, 100)]
pokemon2.attacks = [Attack("Scratch", 0, PHYSICAL, 10, 10, 100)]

# Start Battle
battle = Battle(pokemon1, pokemon2)


def ask_command(pokemon):
    command = None
    while not command:
        # DO_ATTACK -> attack 0
        tmp_command = input(f"What should {pokemon.name} do? ").split(" ")
        if len(tmp_command) == 2:
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = Command({DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass
    return command


def update():
    pass


def load_resources():
    load_pokemon_image(pokemon1, True)
    load_pokemon_image(pokemon2, False)


def render(screen):
    screen.fill((255, 255, 255))
    render_pokemons(screen, pokemon1, pokemon2)
    pygame.display.update()


def load_pokemon_image(pokemon, is_player):
    pokemon_name = pokemon.name.lower()

    if is_player:
        pokemon_img = pygame.image.load('assets/pokemon/' + pokemon_name + "_back.png")
        pokemon_img = pygame.transform.scale(pokemon_img, (300, 300))

        pokemon.renderer = pokemon_img
    else:
        pokemon_img = pygame.image.load('assets/pokemon/' + pokemon_name + "_front.png")
        pokemon_img = pygame.transform.scale(pokemon_img, (300, 300))

        pokemon.renderer = pokemon_img


def render_pokemons(screen, pokemon_1, pokemon_2):
    pokemon_1.render(screen, (20, 300))
    pokemon_2.render(screen, (480, 40))


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 640))
    pygame.display.set_caption("Pykemon")

    load_resources()

    clock = pygame.time.Clock()
    clock.tick(60)
    stopped = False

    while not stopped:
        for event in pygame.event.get():
            if event.type == QUIT:
                stopped = True

        # Main pokemon battle loop
        # First ask for the commands

        '''
        # First for command
        command1 = ask_command(pokemon1)
        command2 = ask_command(pokemon2)
    
        turn = Turn()
        turn.command1 = command1
        turn.command2 = command2
    
        if turn.can_start():
            # Execute turn
            battle.execute_turn(turn)
            battle.print_current_status()
        '''

        update()
        render(screen)


if __name__ == "__main__":
    main()
