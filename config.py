game_stages = [
    {
        "category": "video",
        "video": "./assets/videos/prologue.mp4"
    },
    {
        "category": "interactive",
        "background": "./assets/images/first.png",
        "music": "./assets/audio/music.mp3",
        "enemies": [(500, 380)],
        "player": (200, 380)
    },
    {
        "category": "video",
        "video": "./assets/videos/prologue.mp4"
    },
]

player_config = {
    "ANIMATION_STEPS": [16, 4, 12, 8, 8, 16],
    "ANIM_DEATH": 0,
    "ANIM_HIT": 1,
    "ANIM_IDLE": 4,
    "ANIM_JUMP": 2,
    "ANIM_ATTACK": 5,
    "ANIM_RUN": 3,
    "SIZE_X": 96,
    "SIZE_Y": 96,
    "SCALE": 4,
    "OFFSET": [32, 25],
    "ANIMATION_COOLDOWN": 100,
    "HITBOX_WIDTH": 80,
    "HITBOX_HEIGHT": 180,
    "BASE_SPEED": 5,
    "BASE_HEALTH": 100,
    "JUMP_HEIGHT": 30,
    "VERTICAL_ACCELERATION": 2,
    "VERTICAL_ACCELERATION_LIMIT": (2 ** 9) / 2,
    "GRAVITY": 2,
    "DAMAGE": 20
}

enemy_config = {
    "ANIMATION_STEPS": [16, 21],
    "ANIM_DEATH": 0,
    "ANIM_ATTACK": 1,
    "SIZE_X": 48,
    "SIZE_Y": 80,
    "SCALE": 3,
    "OFFSET": [10, 20],
    "ANIMATION_COOLDOWN": 50,
    "HITBOX_WIDTH": 80,
    "HITBOX_HEIGHT": 180,
    "BASE_SPEED": 5,
    "BASE_HEALTH": 100,
    "DAMAGE": 10
}

colors_config = {
    "HEALTHBAR_MAIN": (255, 255, 0),
    "HEALTHBAR_BG": (0, 0, 0)
}