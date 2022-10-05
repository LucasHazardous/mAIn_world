import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
try:
    import pygame
except ImportError:
    print("pygame is not installed. Install it with 'pip install pygame'")
    quit()
    
from stageLoader import StageLoader
from config import gameStages

def main():
    stageLoader = StageLoader()
    for stage in gameStages:
        if(stage["category"] == "normal"):
            stageLoader.loadNormalStage(**stage)
        elif(stage["category"] == "cutscene"):
            stageLoader.playCutscene(**stage)
        pygame.mixer.music.stop()

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()