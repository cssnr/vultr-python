import os
import re


def get_version() -> str:
    version = os.environ.get("GITHUB_REF_NAME", "0.0.1")
    pattern = r"^\d+\.\d+\.\d+(?:[abc]\d*)?$"
    match = re.match(pattern, version)
    return version if match else "0.0.1"


__version__ = get_version()
