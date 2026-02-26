import requests
from requests.exceptions import RequestException

from .__about__ import __version__

class App:
    def __init__(self):
        self.__VERSION__ = __version__
        self.github_api = "https://api.github.com/repos/jullespio/rajio-sen/releases/latest"
        self.remote_version = ""

    def get_version(self):
        """get the version number as string"""
        return self.__VERSION__

    def get_remote_version(self):
        return self.remote_version

    def is_update_available(self):
        """Checks if the user is using an outdated version of the app from GitHub"""
        try:
            try:
                response = requests.get(self.github_api, timeout=5)
                response.raise_for_status()
                remote_data = response.json()
            except (RequestException, ValueError):
                return False

            if not remote_data or "tag_name" not in remote_data:
                return False

            # GitHub tags often have a 'v' (e.g., 'v3.0.1'). We strip it for the math.
            self.remote_version = remote_data["tag_name"].lstrip('v')

            # compare two version numbers
            try:
                tup_local = tuple(map(int, self.__VERSION__.split(".")))
                tup_remote = tuple(map(int, self.remote_version.split(".")))

                if tup_remote > tup_local:
                    return True
            except (ValueError, IndexError):
                return False

            return False

        except Exception:
            # Silently fail if offline or if you haven't published a release on GitHub yet
            return False