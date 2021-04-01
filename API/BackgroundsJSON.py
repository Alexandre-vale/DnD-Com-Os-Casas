#criado TODOS os backgrounds com base no acolito que o api providencia. Possivel de ter erros na formatação para dicionario


backgrounds = {
    "results": [
        {
                "index": "acolyte",
                "name": "Acolyte",
                "url": "background/acolyte",
                "gold": 15,
                "starting_proficiencies": [
                    {
                        "index": "skill-insight",
                        "name": "Skill: Insight",
                        "url": "/api/proficiencies/skill-insight"
                    },
                    {
                        "index": "skill-religion",
                        "name": "Skill: Religion",
                        "url": "/api/proficiencies/skill-religion"
                    }
                ],
                "language_options": {
                    "from": [
                        {
                            "index": "common",
                            "name": "Common",
                            "url": "/api/languages/common"
                        },
                        {
                            "index": "dwarvish",
                            "name": "Dwarvish",
                            "url": "/api/languages/dwarvish"
                        },
                        {
                            "index": "elvish",
                            "name": "Elvish",
                            "url": "/api/languages/elvish"
                        },
                        {
                            "index": "giant",
                            "name": "Giant",
                            "url": "/api/languages/giant"
                        },
                        {
                            "index": "gnomish",
                            "name": "Gnomish",
                            "url": "/api/languages/gnomish"
                        },
                        {
                            "index": "goblin",
                            "name": "Goblin",
                            "url": "/api/languages/goblin"
                        },
                        {
                            "index": "halfling",
                            "name": "Halfling",
                            "url": "/api/languages/halfling"
                        },
                        {
                            "index": "orc",
                            "name": "Orc",
                            "url": "/api/languages/orc"
                        },
                        {
                            "index": "abyssal",
                            "name": "Abyssal",
                            "url": "/api/languages/abyssal"
                        },
                        {
                            "index": "celestial",
                            "name": "Celestial",
                            "url": "/api/languages/celestial"
                        },
                        {
                            "index": "draconic",
                            "name": "Draconic",
                            "url": "/api/languages/draconic"
                        },
                        {
                            "index": "deep-speech",
                            "name": "Deep Speech",
                            "url": "/api/languages/deep-speech"
                        },
                        {
                            "index": "infernal",
                            "name": "Infernal",
                            "url": "/api/languages/infernal"
                        },
                        {
                            "index": "primordial",
                            "name": "Primordial",
                            "url": "/api/languages/primordial"
                        },
                        {
                            "index": "sylvan",
                            "name": "Sylvan",
                            "url": "/api/languages/sylvan"
                        },
                        {
                            "index": "undercommon",
                            "name": "Undercommon",
                            "url": "/api/languages/undercommon"
                        }
                    ],
                    "choose": 2,
                    "type": "languages"
                },
                "starting_equipment": [
                    {
                        "equipment": {
                            "index": "clothes-common",
                            "name": "Clothes, common",
                            "url": "/api/equipment/clothes-common"
                        },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                            "index": "pouch",
                            "name": "Pouch",
                            "url": "/api/equipment/pouch"
                        },
                        "quantity": 1
                    }
                ],
            "starting_equipment_options": [
                {
                    "choose": 1,
                    "type": "equipment",
                    "from":
                        {
                                "index": "holy-symbols",
                                "name": "Holy Symbols",
                                "url": "/api/equipment-categories/holy-symbols"
                        }
                }
            ]
        },
        {
                "index": "charlatan",
                "name": "Charlatan",
                "url": "background/charlatan",
                "gold": 15,
                "starting_proficiencies": [
                    {
                        "index": "skill-deception",
                        "name": "Skill: Deception",
                        "url": "/api/proficiencies/skill-deception"
                    },
                    {
                        "index": "skill-sleight-of-hand",
                        "name": "Skill: Sleight of hand",
                        "url": "/api/proficiencies/skill-sleight-of-hand"
                    },
                    {
                        "index": "disguise-kit",
                        "name": "Disguise kit",
                        "url": "/api/proficiencies/disguise-kit"
                    },
                    {
                        "index": "forgery-kit",
                        "name": "Forgery kit",
                        "url": "/api/proficiencies/forgery-kit"
                    }
                ],
                "starting_equipment": [
                    {
                        "equipment": {
                            "index": "clothes-fine",
                            "name": "Clothes, fine",
                            "url": "/api/equipment/clothes-fine"
                        },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                            "index": "pouch",
                            "name": "Pouch",
                            "url": "/api/equipment/pouch"
                        },
                        "quantity": 1
                    },
                    { 
                        "equipment": {
                            "index": "disguise-kit",
                            "name": "Disguise Kit",
                            "url": "/api/equipment/disguise-kit"
                        },
                        "quantity": 1
                    },
                ],
        },
        {
                "index": "criminal",
                "name": "Criminal",
                "url": "background/criminal",
                "gold": 15,
                "starting_proficiencies": [
                    {
                        "index": "skill-deception",
                        "name": "Skill: Deception",
                        "url": "/api/proficiencies/skill-deception"
                    },
                    {
                        "index": "skill-stealth",
                        "name": "Skill: Stealth",
                        "url": "/api/proficiencies/skill-stealth"
                    },
                    {
                        "index": "thieves-tools",
                        "name": "Thieves' Tools",
                        "url": "/api/proficiencies/thieves-tools"
                    }
                ],
                "starting_proficiencies_options": [
                    {
                        "choose": 1,
                        "from":{
                                    "index": "gaming-sets",
                                    "name": "Gaming Sets",
                                    "url": "/api/proficiencies/gaming-sets"
                                }
                    }
                ],
                "starting_equipment": [
                    {
                        "equipment": {
                                    "index": "crowbar",
                                    "name": "Crowbar",
                                    "url": "/api/equipment/crowbar"
                                },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                    "index": "clothes-common",
                                    "name": "Clothes, common",
                                    "url": "/api/equipment/clothes-common"
                                },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                            "index": "pouch",
                            "name": "Pouch",
                            "url": "/api/equipment/pouch"
                        },
                        "quantity": 1
                    }
                ],
        },
        {
                "index": "entertainer",
                "name": "Entertainer",
                "url": "background/entertainer",
                "gold": 15,
                "starting_proficiencies": [
                    {
                        "index": "skill-acrobatics",
                        "name": "Skill: Acrobatics",
                        "url": "/api/proficiencies/skill-acrobatics"
                    },
                    {
                        "index": "skill-performance",
                        "name": "Skill: Performance",
                        "url": "/api/proficiencies/skill-performance"
                    },
                    {
                        "index": "disguise-kit",
                        "name": "Disguise kit",
                        "url": "/api/proficiencies/disguise-kit"
                    },
                ],
                "starting_proficiencies_options": [
                    {
                        "choose": 1,
                        "from":{
                                    "index": "musical-instruments",
                                    "name": "Musical Instruments",
                                    "url": "/api/proficiencies/musical-instruments"
                                },
                    }
                ],
                "starting_equipment": [
                    {
                        "equipment": {
                                    "index": "crowbar",
                                    "name": "Crowbar",
                                    "url": "/api/equipment/crowbar"
                                },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                        "index": "clothes-costume",
                                        "name": "Clothes, costume",
                                        "url": "/api/equipment/clothes-costume"
                                    },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                            "index": "pouch",
                            "name": "Pouch",
                            "url": "/api/equipment/pouch"
                        },
                        "quantity": 1
                    }
                ],
                "starting_equipment_options": [
                    {
                        "choose": 1,
                        "from": {
                                    "index": "musical-instruments",
                                    "name": "Musical Instruments",
                                    "url": "/api/equipment-categories/musical-instruments"
                                },
                    }
                ]
        },
        {
                "index": "folk-hero",
                "name": "Folk Hero",
                "url": "background/folk-hero",
                "gold": 10,
                "starting_proficiencies": [
                    {
                        "index": "skill-animal-handling",
                        "name": "Skill: Animal Handling",
                        "url": "/api/proficiencies/skill-animal-handling"
                    },
                    {
                        "index": "skill-survival",
                        "name": "Skill: Survival",
                        "url": "/api/proficiencies/skill-survival"
                    },
                    {
                        "index": "land-vehicles",
                        "name": "Land Vehicles",
                        "url": "/api/proficiencies/land-vehicles"
                    },
                ],
                "starting_proficiencies_options": [
                    {
                        "choose": 1,
                        "from":{
                                    "index": "artisans-tools",
                                    "name": "Artisan's Tools",
                                    "url": "/api/equipment-categories/artisans-tools"
                                },
                    }
                ],
                "starting_equipment": [
                    {
                        "equipment": {
                                        "index": "shovel",
                                        "name": "Shovel",
                                        "url": "/api/equipment/shovel"
                                    },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                        "index": "clothes-common",
                                        "name": "Clothes, common",
                                        "url": "/api/equipment/clothes-common"
                                    },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                        "index": "pot-iron",
                                        "name": "Pot, iron",
                                        "url": "/api/equipment/pot-iron"
                                    },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                            "index": "pouch",
                            "name": "Pouch",
                            "url": "/api/equipment/pouch"
                        },
                        "quantity": 1
                    }
                ],
                "starting_equipment_options": [
                    {
                        "choose": 1,
                        "from": {
                                    "index": "artisans-tools",
                                    "name": "Artisan's Tools",
                                    "url": "/api/equipment-categories/artisans-tools"
                                },
                    }
                ]
        },
        {
                "index": "guild-artisan",
                "name": "Guild Artisan",
                "url": "background/guild-artisan",
                "gold": 15,
                "starting_proficiencies": [
                    {
                        "index": "skill-insight",
                        "name": "Skill: Insight",
                        "url": "/api/proficiencies/skill-insight"
                    },
                    {
                        "index": "skill-persuasion",
                        "name": "Skill: Persuasion",
                        "url": "/api/proficiencies/skill-persuasion"
                    },
                ],
                "starting_proficiencies_options": [
                    {
                        "choose": 1,
                        "from":{
                                    "index": "artisans-tools",
                                    "name": "Artisan's Tools",
                                    "url": "/api/equipment-categories/artisans-tools"
                                },
                    }
                ],
                "language_options": {
                    "from": [
                        {
                            "index": "common",
                            "name": "Common",
                            "url": "/api/languages/common"
                        },
                        {
                            "index": "dwarvish",
                            "name": "Dwarvish",
                            "url": "/api/languages/dwarvish"
                        },
                        {
                            "index": "elvish",
                            "name": "Elvish",
                            "url": "/api/languages/elvish"
                        },
                        {
                            "index": "giant",
                            "name": "Giant",
                            "url": "/api/languages/giant"
                        },
                        {
                            "index": "gnomish",
                            "name": "Gnomish",
                            "url": "/api/languages/gnomish"
                        },
                        {
                            "index": "goblin",
                            "name": "Goblin",
                            "url": "/api/languages/goblin"
                        },
                        {
                            "index": "halfling",
                            "name": "Halfling",
                            "url": "/api/languages/halfling"
                        },
                        {
                            "index": "orc",
                            "name": "Orc",
                            "url": "/api/languages/orc"
                        },
                        {
                            "index": "abyssal",
                            "name": "Abyssal",
                            "url": "/api/languages/abyssal"
                        },
                        {
                            "index": "celestial",
                            "name": "Celestial",
                            "url": "/api/languages/celestial"
                        },
                        {
                            "index": "draconic",
                            "name": "Draconic",
                            "url": "/api/languages/draconic"
                        },
                        {
                            "index": "deep-speech",
                            "name": "Deep Speech",
                            "url": "/api/languages/deep-speech"
                        },
                        {
                            "index": "infernal",
                            "name": "Infernal",
                            "url": "/api/languages/infernal"
                        },
                        {
                            "index": "primordial",
                            "name": "Primordial",
                            "url": "/api/languages/primordial"
                        },
                        {
                            "index": "sylvan",
                            "name": "Sylvan",
                            "url": "/api/languages/sylvan"
                        },
                        {
                            "index": "undercommon",
                            "name": "Undercommon",
                            "url": "/api/languages/undercommon"
                        }
                    ],
                    "choose": 1,
                    "type": "languages"
                },
                "starting_equipment": [
                    {
                        "equipment": {
                                        "index": "clothes-travelers",
                                        "name": "Clothes, traveler's",
                                        "url": "/api/equipment/clothes-travelers"
                                    },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                            "index": "pouch",
                            "name": "Pouch",
                            "url": "/api/equipment/pouch"
                        },
                        "quantity": 1
                    }
                ],
                "starting_equipment_options": [
                    {
                        "choose": 1,
                        "from": {
                                    "index": "artisans-tools",
                                    "name": "Artisan's Tools",
                                    "url": "/api/equipment-categories/artisans-tools"
                                },
                    }
                ]
        },
        {
                "index": "hermit",
                "name": "Hermit",
                "url": "background/hermit",
                "gold": 5,
                "starting_proficiencies": [
                    {
                        "index": "skill-medicine",
                        "name": "Skill: Medicine",
                        "url": "/api/proficiencies/skill-medicine"
                    },
                    {
                        "index": "skill-religion",
                        "name": "Skill: Religion",
                        "url": "/api/proficiencies/skill-religion"
                    },
                    {
                        "index": "herbalism-kit",
                        "name": "Herbalism Kit",
                        "url": "/api/proficiencies/herbalism-kit"
                    }
                ],
                "language_options": {
                    "from": [
                        {
                            "index": "common",
                            "name": "Common",
                            "url": "/api/languages/common"
                        },
                        {
                            "index": "dwarvish",
                            "name": "Dwarvish",
                            "url": "/api/languages/dwarvish"
                        },
                        {
                            "index": "elvish",
                            "name": "Elvish",
                            "url": "/api/languages/elvish"
                        },
                        {
                            "index": "giant",
                            "name": "Giant",
                            "url": "/api/languages/giant"
                        },
                        {
                            "index": "gnomish",
                            "name": "Gnomish",
                            "url": "/api/languages/gnomish"
                        },
                        {
                            "index": "goblin",
                            "name": "Goblin",
                            "url": "/api/languages/goblin"
                        },
                        {
                            "index": "halfling",
                            "name": "Halfling",
                            "url": "/api/languages/halfling"
                        },
                        {
                            "index": "orc",
                            "name": "Orc",
                            "url": "/api/languages/orc"
                        },
                        {
                            "index": "abyssal",
                            "name": "Abyssal",
                            "url": "/api/languages/abyssal"
                        },
                        {
                            "index": "celestial",
                            "name": "Celestial",
                            "url": "/api/languages/celestial"
                        },
                        {
                            "index": "draconic",
                            "name": "Draconic",
                            "url": "/api/languages/draconic"
                        },
                        {
                            "index": "deep-speech",
                            "name": "Deep Speech",
                            "url": "/api/languages/deep-speech"
                        },
                        {
                            "index": "infernal",
                            "name": "Infernal",
                            "url": "/api/languages/infernal"
                        },
                        {
                            "index": "primordial",
                            "name": "Primordial",
                            "url": "/api/languages/primordial"
                        },
                        {
                            "index": "sylvan",
                            "name": "Sylvan",
                            "url": "/api/languages/sylvan"
                        },
                        {
                            "index": "undercommon",
                            "name": "Undercommon",
                            "url": "/api/languages/undercommon"
                        }
                    ],
                    "choose": 1,
                    "type": "languages"
                },
                "starting_equipment": [
                    {
                        "equipment": {
                                        "index": "clothes-common",
                                        "name": "Clothes, Common",
                                        "url": "/api/equipment/clothes-common"
                                    },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                "index": "blanket",
                                "name": "Blanket",
                                "url": "/api/equipment/blanket"
                            },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                "index": "herbalism-kit",
                                "name": "Herbalism Kit",
                                "url": "/api/equipment/herbalism-kit"
                            },
                        "quantity": 1
                    }
                ],
        },
        {
                "index": "noble",
                "name": "Noble",
                "url": "background/noble",
                "gold": 25,
                "starting_proficiencies": [
                    {
                        "index": "skill-persuasion",
                        "name": "Skill: Persuasion",
                        "url": "/api/proficiencies/skill-persuasion"
                    },
                    {
                        "index": "skill-history",
                        "name": "Skill: History",
                        "url": "/api/proficiencies/skill-history"
                    },
                ],
                "starting_proficiencies_options": [
                    {
                        "choose": 1,
                        "from":{
                                    "index": "gaming-sets",
                                    "name": "Gaming Sets",
                                    "url": "/api/proficiencies/gaming-sets"
                                }
                    }
                ],
                "language_options": {
                    "from": [
                        {
                            "index": "common",
                            "name": "Common",
                            "url": "/api/languages/common"
                        },
                        {
                            "index": "dwarvish",
                            "name": "Dwarvish",
                            "url": "/api/languages/dwarvish"
                        },
                        {
                            "index": "elvish",
                            "name": "Elvish",
                            "url": "/api/languages/elvish"
                        },
                        {
                            "index": "giant",
                            "name": "Giant",
                            "url": "/api/languages/giant"
                        },
                        {
                            "index": "gnomish",
                            "name": "Gnomish",
                            "url": "/api/languages/gnomish"
                        },
                        {
                            "index": "goblin",
                            "name": "Goblin",
                            "url": "/api/languages/goblin"
                        },
                        {
                            "index": "halfling",
                            "name": "Halfling",
                            "url": "/api/languages/halfling"
                        },
                        {
                            "index": "orc",
                            "name": "Orc",
                            "url": "/api/languages/orc"
                        },
                        {
                            "index": "abyssal",
                            "name": "Abyssal",
                            "url": "/api/languages/abyssal"
                        },
                        {
                            "index": "celestial",
                            "name": "Celestial",
                            "url": "/api/languages/celestial"
                        },
                        {
                            "index": "draconic",
                            "name": "Draconic",
                            "url": "/api/languages/draconic"
                        },
                        {
                            "index": "deep-speech",
                            "name": "Deep Speech",
                            "url": "/api/languages/deep-speech"
                        },
                        {
                            "index": "infernal",
                            "name": "Infernal",
                            "url": "/api/languages/infernal"
                        },
                        {
                            "index": "primordial",
                            "name": "Primordial",
                            "url": "/api/languages/primordial"
                        },
                        {
                            "index": "sylvan",
                            "name": "Sylvan",
                            "url": "/api/languages/sylvan"
                        },
                        {
                            "index": "undercommon",
                            "name": "Undercommon",
                            "url": "/api/languages/undercommon"
                        }
                    ],
                    "choose": 1,
                    "type": "languages"
                },
                "starting_equipment": [
                    {
                        "equipment": {
                                        "index": "clothes-fine",
                                        "name": "Clothes, Fine",
                                        "url": "/api/equipment/clothes-fine"
                                    },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                    "index": "signet-ring",
                                    "name": "Signet ring",
                                    "url": "/api/equipment/signet-ring"
                                },
                        "quantity": 1
                    },
                ],
        },
        {
                "index": "outlander",
                "name": "Outlander",
                "url": "background/outlander",
                "gold": 10,
                "starting_proficiencies": [
                    {
                        "index": "skill-athletics",
                        "name": "Skill: Athletics",
                        "url": "/api/proficiencies/skill-athletics"
                    },
                    {
                        "index": "skill-survival",
                        "name": "Skill: Survival",
                        "url": "/api/proficiencies/skill-survival"
                    },
                ],
                "starting_proficiencies_options": [
                    {
                        "choose": 1,
                        "from":{
                                    "index": "musical-instruments",
                                    "name": "Musical Instruments",
                                    "url": "/api/proficiencies/musical-instruments"
                                }
                    }
                ],
                "language_options": {
                    "from": [
                        {
                            "index": "common",
                            "name": "Common",
                            "url": "/api/languages/common"
                        },
                        {
                            "index": "dwarvish",
                            "name": "Dwarvish",
                            "url": "/api/languages/dwarvish"
                        },
                        {
                            "index": "elvish",
                            "name": "Elvish",
                            "url": "/api/languages/elvish"
                        },
                        {
                            "index": "giant",
                            "name": "Giant",
                            "url": "/api/languages/giant"
                        },
                        {
                            "index": "gnomish",
                            "name": "Gnomish",
                            "url": "/api/languages/gnomish"
                        },
                        {
                            "index": "goblin",
                            "name": "Goblin",
                            "url": "/api/languages/goblin"
                        },
                        {
                            "index": "halfling",
                            "name": "Halfling",
                            "url": "/api/languages/halfling"
                        },
                        {
                            "index": "orc",
                            "name": "Orc",
                            "url": "/api/languages/orc"
                        },
                        {
                            "index": "abyssal",
                            "name": "Abyssal",
                            "url": "/api/languages/abyssal"
                        },
                        {
                            "index": "celestial",
                            "name": "Celestial",
                            "url": "/api/languages/celestial"
                        },
                        {
                            "index": "draconic",
                            "name": "Draconic",
                            "url": "/api/languages/draconic"
                        },
                        {
                            "index": "deep-speech",
                            "name": "Deep Speech",
                            "url": "/api/languages/deep-speech"
                        },
                        {
                            "index": "infernal",
                            "name": "Infernal",
                            "url": "/api/languages/infernal"
                        },
                        {
                            "index": "primordial",
                            "name": "Primordial",
                            "url": "/api/languages/primordial"
                        },
                        {
                            "index": "sylvan",
                            "name": "Sylvan",
                            "url": "/api/languages/sylvan"
                        },
                        {
                            "index": "undercommon",
                            "name": "Undercommon",
                            "url": "/api/languages/undercommon"
                        }
                    ],
                    "choose": 1,
                    "type": "languages"
                },
                "starting_equipment": [
                    {
                        "equipment": {
                                        "index": "clothes-travelers",
                                        "name": "Clothes, Traveler's",
                                        "url": "/api/equipment/clothes-travelers"
                                    },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                    "index": "staff",
                                    "name": "Staff",
                                    "url": "/api/equipment/staff"
                                },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                    "index": "hunting-trap",
                                    "name": "Hunting trap",
                                    "url": "/api/equipment/hunting-trap"
                                },
                        "quantity": 1
                    },
                ],
        },
        {
                "index": "sage",
                "name": "Sage",
                "url": "background/sage",
                "gold": 10,
                "starting_proficiencies": [
                    {
                        "index": "skill-arcana",
                        "name": "Skill: Arcana",
                        "url": "/api/proficiencies/skill-arcana"
                    },
                    {
                        "index": "skill-history",
                        "name": "Skill: History",
                        "url": "/api/proficiencies/skill-history"
                    },
                ],
                "language_options": {
                    "from": [
                        {
                            "index": "common",
                            "name": "Common",
                            "url": "/api/languages/common"
                        },
                        {
                            "index": "dwarvish",
                            "name": "Dwarvish",
                            "url": "/api/languages/dwarvish"
                        },
                        {
                            "index": "elvish",
                            "name": "Elvish",
                            "url": "/api/languages/elvish"
                        },
                        {
                            "index": "giant",
                            "name": "Giant",
                            "url": "/api/languages/giant"
                        },
                        {
                            "index": "gnomish",
                            "name": "Gnomish",
                            "url": "/api/languages/gnomish"
                        },
                        {
                            "index": "goblin",
                            "name": "Goblin",
                            "url": "/api/languages/goblin"
                        },
                        {
                            "index": "halfling",
                            "name": "Halfling",
                            "url": "/api/languages/halfling"
                        },
                        {
                            "index": "orc",
                            "name": "Orc",
                            "url": "/api/languages/orc"
                        },
                        {
                            "index": "abyssal",
                            "name": "Abyssal",
                            "url": "/api/languages/abyssal"
                        },
                        {
                            "index": "celestial",
                            "name": "Celestial",
                            "url": "/api/languages/celestial"
                        },
                        {
                            "index": "draconic",
                            "name": "Draconic",
                            "url": "/api/languages/draconic"
                        },
                        {
                            "index": "deep-speech",
                            "name": "Deep Speech",
                            "url": "/api/languages/deep-speech"
                        },
                        {
                            "index": "infernal",
                            "name": "Infernal",
                            "url": "/api/languages/infernal"
                        },
                        {
                            "index": "primordial",
                            "name": "Primordial",
                            "url": "/api/languages/primordial"
                        },
                        {
                            "index": "sylvan",
                            "name": "Sylvan",
                            "url": "/api/languages/sylvan"
                        },
                        {
                            "index": "undercommon",
                            "name": "Undercommon",
                            "url": "/api/languages/undercommon"
                        }
                    ],
                    "choose": 2,
                    "type": "languages"
                },
                "starting_equipment": [
                    {
                        "equipment": {
                                        "index": "clothes-common",
                                        "name": "Clothes, Common",
                                        "url": "/api/equipment/clothes-common"
                                    },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                    "index": "ink-1-ounce-bottle",
                                    "name": "Ink (1 ounce bottle)",
                                    "url": "/api/equipment/ink-1-ounce-bottle"
                                },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                    "index": "ink-pen",
                                    "name": "Ink pen",
                                    "url": "/api/equipment/ink-pen"
                                },
                        "quantity": 1
                    },
                ],
        },
        {
                "index": "sailor",
                "name": "Sailor",
                "url": "background/sailor",
                "gold": 10,
                "starting_proficiencies": [
                    {
                        "index": "skill-athletics",
                        "name": "Skill: Athletics",
                        "url": "/api/proficiencies/skill-athletics"
                    },
                    {
                        "index": "skill-perception",
                        "name": "Skill: Perception",
                        "url": "/api/proficiencies/skill-perception"
                    },
                    {
                        "index": "water-vehicles",
                        "name": "Water Vehicles",
                        "url": "/api/proficiencies/water-vehicles"
                    },
                    {
                        "index": "navigators-tools",
                        "name": "Navigator's Tools",
                        "url": "/api/proficiencies/navigators-tools"
                    },
                ],
                "starting_equipment": [
                    {
                        "equipment": {
                                        "index": "clothes-common",
                                        "name": "Clothes, Common",
                                        "url": "/api/equipment/clothes-common"
                                    },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                        "index": "rope-silk-50-feet",
                                        "name": "Rope, silk (50 feet)",
                                        "url": "/api/equipment/rope-silk-50-feet"
                                    },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                    "index": "ink-pen",
                                    "name": "Ink pen",
                                    "url": "/api/equipment/ink-pen"
                                },
                        "quantity": 1
                    },
                ],
        },
        {
                "index": "soldier",
                "name": "Soldier",
                "url": "background/soldier",
                "gold": 10,
                "starting_proficiencies": [
                    {
                        "index": "skill-athletics",
                        "name": "Skill: Athletics",
                        "url": "/api/proficiencies/skill-athletics"
                    },
                    {
                        "index": "skill-intimidation",
                        "name": "Skill: Intimidation",
                        "url": "/api/proficiencies/skill-intimidation"
                    },
                    {
                        "index": "land-vehicles",
                        "name": "Land Vehicles",
                        "url": "/api/proficiencies/land-vehicles"
                    },
                ],
                "starting_proficiencies_options": [
                    {
                        "choose": 1,
                        "from":{
                                    "index": "gaming-sets",
                                    "name": "Gaming Sets",
                                    "url": "/api/equipment-categories/gaming-sets"
                                },
                    }
                ],
                "starting_equipment": [
                    {
                        "equipment": {
                                        "index": "clothes-common",
                                        "name": "Clothes, Common",
                                        "url": "/api/equipment/clothes-common"
                                    },
                        "quantity": 1
                    },
                    {
                        "equipment": {
                                "index": "dice-set",
                                "name": "Dice set",
                                "url": "/api/equipment/dice-set"
                            },
                        "quantity": 1
                    },
                ],
        },
    ]
}