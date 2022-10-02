try:
    import pygame
except ImportError:
    print("pygame is not installed. Install it with 'pip install pygame'")
    quit()
    
from stageLoader import StageLoader
from config import game_stages

def main():
    stageLoader = StageLoader()
    for stage in game_stages:
        if(stage["category"] in ("normal", "bossFight")):
            stageLoader.loadInteractiveStage(**stage)
        elif(stage["category"] == "cutscene"):
            stageLoader.playCutscene(**stage)
        pygame.mixer.music.stop()

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()