gameSettings = {
    "SCREEN_WIDTH": 1000,
    "SCREEN_HEIGHT": 600,
    "FPS": 60,
    "DEPTH": 24,
    "SPRITESHEET_PATH": "./assets/images/entities/"
}

gameStages = [
    {
        "category": "cutscene",
        "audio": "./assets/audio/introduction.mp3",
        "background": "./assets/images/stages/bar.png"
    },
    {
        "category": "normal",
        "background": "./assets/images/stages/abandoned1.png",
        "audio": "",
        "playerPos": (100, 380)
    },
    {
        "category": "normal",
        "background": "./assets/images/stages/abandoned2.png",
        "audio": "./assets/audio/cyber-attack.mp3",
        "shootingEnemiesPos": [(600, 380), (800, 380)],
        "playerPos": (50, 380)
    },
    {
        "category": "normal",
        "background": "./assets/images/stages/park.png",
        "audio": "./assets/audio/80s-synth-wave.mp3",
        "playerPos": (100, 380)
    },
    {
        "category": "normal",
        "background": "./assets/images/stages/building.png",
        "audio": "./assets/audio/cyber-attack.mp3",
        "shootingEnemiesPos": [(500, 380), (600, 380), (800, 380)],
        "playerPos": (50, 380)
    },
    {
        "category": "normal",
        "background": "./assets/images/stages/lobby.png",
        "audio": "./assets/audio/trap-auto-drift-sport.mp3",
        "playerPos": (50, 380)
    },
    {
        "category": "cutscene",
        "audio": "./assets/audio/boss-dialogue.mp3",
        "background": "./assets/images/stages/boss-meeting.jpg"
    },
    {
        "category": "normal",
        "background": "./assets/images/stages/skyscraper.png",
        "audio": "./assets/audio/cyberpunk-electro-sport-atomic.mp3",
        "bossPos": (500, 380),
        "playerPos": (200, 380)
    },
    {
        "category": "normal",
        "background": "./assets/images/stages/exit.png",
        "audio": "./assets/audio/endless-party.mp3",
        "playerPos": (50, 380)
    },
    {
        "category": "normal",
        "background": "./assets/images/stages/tunnel.png",
        "audio": "./assets/audio/no-limits.mp3",
        "playerPos": (50, 380),
        "walkingEnemiesPos": [(700, 380)]
    },
    {
        "category": "normal",
        "background": "./assets/images/stages/junkyard.png",
        "audio": "./assets/audio/no-limits.mp3",
        "playerPos": (50, 380),
        "walkingEnemiesPos": [(0, 380), (700, 380)],
        "shootingEnemiesPos": [(200, 380)]
    },
    {
        "category": "cutscene",
        "audio": "./assets/audio/boss-dialogue2.mp3",
        "background": "./assets/images/stages/boss-meeting2.jpg"
    },
    {
        "category": "normal",
        "background": "./assets/images/stages/highway.png",
        "audio": "./assets/audio/cinematic-metal.mp3",
        "bossPos": (700, 380),
        "playerPos": (200, 380)
    },
    {
        "category": "cutscene",
        "audio": "./assets/audio/guardian-dialogue.mp3",
        "background": "./assets/images/stages/guardianMeeting.jpg"
    },
    {
        "category": "normal",
        "background": "./assets/images/stages/highway.png",
        "audio": "./assets/audio/cinematic-metal.mp3",
        "guardianPos": (700, 380),
        "playerPos": (200, 380)
    },
    {
        "category": "cutscene",
        "audio": "./assets/audio/final-boss-dialogue.mp3",
        "background": "./assets/images/stages/finalBossMeeting.jpg"
    },
    {
        "category": "normal",
        "background": "./assets/images/stages/exit.png",
        "audio": "./assets/audio/80s-synth-wave.mp3",
        "finalBossPos": (700, 380),
        "playerPos": (200, 380)
    }
]

playerConfig = {
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

shootingEnemyConfig = {
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
    "BASE_HEALTH": 100
}

walkingEnemyConfig = {
    "ANIMATION_STEPS": [5],
    "ANIM_WALK": 0,
    "SIZE_X": 82,
    "SIZE_Y": 104,
    "SCALE": 2,
    "OFFSET": [10, 10],
    "ANIMATION_COOLDOWN": 50,
    "HITBOX_WIDTH": 120,
    "HITBOX_HEIGHT": 180,
    "BASE_HEALTH": 200,
    "SPEED": 2,
    "ATTACK_WIDTH": 10,
    "DAMAGE": 1
}

bossConfig = {
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

guardianConfig = {
    "ANIMATION_STEPS": [8, 6, 6],
    "ANIM_DEATH": 2,
    "ANIM_RUN": 0,
    "ANIM_ATTACK": 1,
    "SIZE_X": 200,
    "SIZE_Y": 200,
    "SCALE": 3,
    "OFFSET": [85, 70],
    "ANIMATION_COOLDOWN": 100,
    "HITBOX_WIDTH": 96,
    "HITBOX_HEIGHT": 180,
    "BASE_SPEED": 5,
    "BASE_HEALTH": 300,
    "DAMAGE": 10,
    "SPEED": 4,
    "ATTACK_FRAME": 4
}

finalBossConfig = {
    "ANIMATION_STEPS": [8, 4, 7],
    "ANIM_DEATH": 2,
    "ANIM_RUN": 0,
    "ANIM_ATTACK": 1,
    "ANIM_HIT": 3,
    "SIZE_X": 200,
    "SIZE_Y": 200,
    "SCALE": 3,
    "OFFSET": [85, 70],
    "ANIMATION_COOLDOWN": 100,
    "HITBOX_WIDTH": 96,
    "HITBOX_HEIGHT": 180,
    "BASE_SPEED": 5,
    "BASE_HEALTH": 150,
    "DAMAGE": 10,
    "SPEED": 4,
    "ATTACK_FRAME": 3
}

projectileConfig = {
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

empConfig = {
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

colorsConfig = {
    "HEALTHBAR_MAIN": (255, 255, 0),
    "HEALTHBAR_BG": (0, 0, 0)
}