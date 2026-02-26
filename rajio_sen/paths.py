import os
import shutil
import sys
from rajio_sen.logger import log


def get_user_home():
    """Get the user's home directory in a cross-platform way."""
    return os.path.expanduser("~")


def get_base_dir():
    """
    Return the base directory for rajio_sen files: ~/rajio_sen
    """
    home = get_user_home()
    base_dir = os.path.join(home, "rajio_sen")

    try:
        os.makedirs(base_dir, exist_ok=True)
    except Exception as e:
        log.error(f"Could not create base directory {base_dir}: {e}")

    return base_dir


def _migrate_file(legacy_path, new_path, description):
    """Migrate a file from legacy_path to new_path if it exists."""
    if os.path.exists(legacy_path) and not os.path.exists(new_path):
        log.info(f"ＭＩＧＲＡＴＩＯＮ: Moving {description} to {new_path}")
        try:
            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            shutil.move(legacy_path, new_path)
        except Exception as e:
            log.warning(f"Could not migrate {description}: {e}")


def get_config_path():
    """Path to config.ini. Migrates from legacy dotfiles and old folder names."""
    base_dir = get_base_dir()
    new_path = os.path.join(base_dir, "config.ini")
    home = get_user_home()

    # Legacy targets
    _migrate_file(os.path.join(home, ".radio-active-configs.ini"), new_path, "legacy dot-config")
    _migrate_file(os.path.join(home, "radioactive", "config.ini"), new_path, "legacy folder-config")
    _migrate_file(os.path.join(home, ".config", "radio-active", "config.ini"), new_path, "XDG legacy config")

    return new_path


def get_alias_path():
    """Path to alias_map (favorites)."""
    base_dir = get_base_dir()
    new_path = os.path.join(base_dir, "alias_map")
    home = get_user_home()

    # Legacy targets
    _migrate_file(os.path.join(home, ".radio-active-alias"), new_path, "legacy dot-alias")
    _migrate_file(os.path.join(home, "radioactive", "alias_map"), new_path, "legacy folder-alias")
    _migrate_file(os.path.join(home, ".config", "radio-active", "alias_map"), new_path, "XDG legacy alias")

    return new_path


def get_last_station_path():
    """Path to last_station tracker."""
    base_dir = get_base_dir()
    new_path = os.path.join(base_dir, "last_station")
    home = get_user_home()

    # Legacy targets
    _migrate_file(os.path.join(home, ".radio-active-last_station"), new_path, "legacy dot-last-station")
    _migrate_file(os.path.join(home, "radioactive", "last_station"), new_path, "legacy folder-last-station")
    
    return new_path


def get_recordings_path():
    """Path for recordings: ~/rajio_sen/recordings"""
    base_dir = get_base_dir()
    recordings_path = os.path.join(base_dir, "recordings")

    # If the old recordings folder exists, we might want to move it too
    home = get_user_home()
    old_recordings = os.path.join(home, "radioactive", "recordings")
    if os.path.exists(old_recordings) and not os.path.exists(recordings_path):
         _migrate_file(old_recordings, recordings_path, "legacy recordings directory")

    try:
        os.makedirs(recordings_path, exist_ok=True)
    except Exception as e:
        log.error(f"Could not create recordings directory {recordings_path}: {e}")

    return recordings_path