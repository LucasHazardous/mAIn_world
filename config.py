game_stages = [
    {
        "category": "interactive",
        "background": "./assets/images/first.png",
        "music": "./assets/audio/music.mp3",
        "enemies": [(500, 380)],
        "player": (200, 380)
    },
    {
        "category": "video",
        "video": "./assets/videos/"
    }
]

player_config = {
    "PLAYER_ANIMATION_STEPS": [16, 4, 12, 8, 8, 16],
    "ANIM_DEATH": 0,
    "ANIM_HIT": 1,
    "ANIM_IDLE": 4,
    "ANIM_JUMP": 2,
    "ANIM_ATTACK": 5,
    "ANIM_RUN": 3,
    "PLAYER_SIZE": 96,
    "PLAYER_SCALE": 4,
    "PLAYER_OFFSET": [32, 25],
    "ANIMATION_COOLDOWN": 100,
    "HITBOX_WIDTH": 80,
    "HITBOX_HEIGHT": 180,
    "BASE_SPEED": 5,
    "BASE_HEALTH": 100,
    "JUMP_HEIGHT": 30,
    "VERTICAL_ACCELERATION": 2,
    "VERTICAL_ACCELERATION_LIMIT": (2 ** 9) / 2,
    "PLAYER_GRAVITY": 2
}