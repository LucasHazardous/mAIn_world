import pygame
from stageLoader import StageLoader
from config import game_stages

def main():
    stageLoader = StageLoader()
    for stage in game_stages:
        if(stage["category"] == "interactive"):
            stageLoader.playInteractiveStage(stage["background"], stage["music"], stage["player"], stage["enemies"])
        elif(stage["category"] == "cutscene"):
            stageLoader.playCutscene(stage["audio"], stage["image"])
        elif(stage["category"] == "boss"):
            stageLoader.playBossFight(stage["background"], stage["music"], stage["player"], stage["boss"])
        pygame.mixer.music.stop()

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()