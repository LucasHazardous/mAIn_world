import pygame
from stageLoader import StageLoader
from config import game_stages

def main():
    stageLoader = StageLoader()
    for stage in game_stages:
        if(stage["category"] == "interactive"):
            stageLoader.loadStage(stage["background"], stage["music"], stage["player"], stage["enemies"])

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()