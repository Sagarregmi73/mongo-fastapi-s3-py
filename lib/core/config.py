import os
from pathlib import Path

class Config:
    def __init__(self):
        env = os.getenv("APP_ENV", "local")
        prop_path = Path(__file__).parent.parent.parent / "env" / f".{env}.properties"
        if not prop_path.exists():
            raise FileNotFoundError(f"Properties file not found: {prop_path}")
        self.props = self._load_properties(prop_path)

    def _load_properties(self, path):
        props = {}
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    if '=' in line:
                        k, v = line.split("=", 1)
                        props[k.strip()] = v.strip()
        return props

    def get(self, key, default=None):
        return self.props.get(key, default)

config = Config()
