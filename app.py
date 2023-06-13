from phrasehunter import game
import settings

if __name__ == '__main__':
    if settings.debug:
        print(settings.debug_warning)
    if settings.DIFFICULTY == 1:
        print(settings.difficulty_warning)
    while True:
        game_class = game.Game()
        play_again = game_class.start()
        if not play_again:
            print("\nThank you for playing! Goodbye")
            break


