from expenses_logger.helper import get_app_major_version

DATABASE_FILE = f"db_v{get_app_major_version()}.X.sqlite3"
SYNC_NAS_DIR = "/home/pi/myNAS/myShare/"
SYNC_NAS_DIR = "c:/tmp/"
DATABASE_URL = f"sqlite:////home/pi/Desktop/apps/{DATABASE_FILE}"
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"
USERS = [
    "Name 1",
    "Name 2",
]
