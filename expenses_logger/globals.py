from pathlib import Path

from expenses_logger.logic.helper import get_app_major_version

WORKING_DIR = Path(__file__).parent.parent
DATABASE_FILE = f"db_v{get_app_major_version()}.X.sqlite3"
SYNC_NAS_DIR = "/home/pi/myNAS/myShare/"
SYNC_NAS_DIR = "c:/tmp/"
DATABASE_URL = f"sqlite:////home/pi/Desktop/apps/{DATABASE_FILE}"
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"
USERS = [
    "Name 1",
    "Name 2",
]
