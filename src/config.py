game_stages = [
    {
        "category": "cutscene",
        "audio": "./assets/audio/introduction.mp3",
        "image": "./assets/images/stages/bar.png"
    },
    {
        "category": "interactive",
        "background": "./assets/images/stages/abandoned1.png",
        "music": "",
        "enemies": [],
        "player": (100, 380)
    },
    {
        "category": "interactive",
        "background": "./assets/images/stages/abandoned2.png",
        "music": "./assets/audio/cyber-attack.mp3",
        "enemies": [(600, 380), (800, 380)],
        "player": (50, 380)
    },
    {
        "category": "interactive",
        "background": "./assets/images/stages/park.png",
        "music": "./assets/audio/80s-synth-wave.mp3",
        "enemies": [],
        "player": (100, 380)
    },
    {
        "category": "interactive",
        "background": "./assets/images/stages/building.png",
        "music": "./assets/audio/cyber-attack.mp3",
        "enemies": [(500, 380), (600, 380), (800, 380)],
        "player": (50, 380)
    },
    {
        "category": "interactive",
        "background": "./assets/images/stages/lobby.png",
        "music": "./assets/audio/trap-auto-drift-sport.mp3",
        "enemies": [],
        "player": (50, 380)
    },
    {
        "category": "cutscene",
        "audio": "./assets/audio/boss-dialogue.mp3",
        "image": "./assets/images/stages/boss-meeting.jpg"
    },
    {
        "category": "boss",
        "background": "./assets/images/stages/skyscraper.png",
        "music": "./assets/audio/cyberpunk-electro-sport-atomic.mp3",
        "boss": (500, 380),
        "player": (200, 380)
    },
    {
        "category": "interactive",
        "background": "./assets/images/stages/exit.png",
        "music": "./assets/audio/endless-party.mp3",
        "enemies": [],
        "player": (50, 380)
    }
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
    "DAMAGE": 20,
    "EMP_DAMAGE": 80
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
    "BASE_HEALTH": 100
}

boss_config = {
    "ANIMATION_STEPS": [16, 10, 10],
    "ANIM_DEATH": 0,
    "ANIM_RUN": 1,
    "ANIM_DASH": 2,
    "SIZE_X": 64,
    "SIZE_Y": 64,
    "SCALE": 4,
    "OFFSET": [20, 0],
    "ANIMATION_COOLDOWN": 100,
    "HITBOX_WIDTH": 96,
    "HITBOX_HEIGHT": 180,
    "BASE_SPEED": 5,
    "BASE_HEALTH": 500,
    "DAMAGE": 10,
    "ANIM_DASH_ATTACK_FRAME": 5,
    "SPEED": 4,
    "TELEPORT_RANGE": (100, 800)
}

projectile_config = {
    "SPEED": 20,
    "ANIMATION_STEPS": [45],
    "SIZE_X": 64,
    "SIZE_Y": 64,
    "OFFSET": [0, 0],
    "ANIMATION_COOLDOWN": 20,
    "HITBOX_WIDTH": 64,
    "HITBOX_HEIGHT": 64,
    "BASE_HEALTH": 0,
    "ANIM_FLY": 0,
    "SCALE": 1,
    "DAMAGE": 20
}

emp_config = {
    "ANIMATION_STEPS": [28],
    "SIZE_X": 96,
    "SIZE_Y": 96,
    "OFFSET": [0, 0],
    "ANIMATION_COOLDOWN": 20,
    "HITBOX_WIDTH": 192,
    "HITBOX_HEIGHT": 192,
    "BASE_HEALTH": 1,
    "ANIM_BLAST": 0,
    "SCALE": 2,
    "DAMAGE": 0
}

colors_config = {
    "HEALTHBAR_MAIN": (255, 255, 0),
    "HEALTHBAR_BG": (0, 0, 0)
}