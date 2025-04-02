import json
from pathlib import Path

def load_lottie(filepath):
    """Load Lottie animation JSON file"""
    with open(filepath, "r") as f:
        return json.load(f)

def get_animation(animation_name):
    """Get built-in animations"""
    animations = {
        "loading": {
            # Simple loading spinner as fallback
            "v": "5.5.2",
            "fr": 60,
            "ip": 0,
            "op": 60,
            "w": 200,
            "h": 200,
            "nm": "Loading",
            "layers": [
                {
                    "ty": 4,
                    "nm": "Loading Circle",
                    "shapes": [
                        {
                            "ty": "el",
                            "p": {"a": 0, "k": [100, 100]},
                            "s": {"a": 0, "k": [80, 80]},
                            "st": 0,
                            "sw": 8,
                            "c": {"a": 0, "k": [1, 0.5, 0.3, 1]}
                        }
                    ],
                    "sr": 1,
                    "ks": {
                        "o": {"a": 1, "k": [
                            {"i": {"x": [0.833], "y": [0.833]}, "o": {"x": [0.167], "y": [0.167]}, "t": 0, "s": [0]},
                            {"t": 60, "s": [100]}
                        ]},
                        "r": {"a": 1, "k": [
                            {"i": {"x": [0.667], "y": [1]}, "o": {"x": [0.333], "y": [0]}, "t": 0, "s": [0]},
                            {"t": 60, "s": [360]}
                        ]}
                    }
                }
            ]
        }
    }
    return animations.get(animation_name)