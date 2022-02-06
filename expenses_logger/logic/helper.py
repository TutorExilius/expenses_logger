import asyncio
from datetime import datetime
from pathlib import Path

import expenses_logger.globals as globals
import toml
from aiofile import async_open

in_syncing_lock = asyncio.Lock()


def print_log(page_name: str, username: str, action: str) -> None:
    print(
        f"{datetime.now():%Y-%m-%d %H:%M:%S} from [{page_name}]: '{username}' {action}."
    )


def max_digits_behind_comma_arrived(amount: str) -> bool:
    splitted_amout = amount.split(",")
    return len(splitted_amout) > 1 and len(splitted_amout[1]) > 1


def amount_in_cents_to_str(amount_in_cents: int) -> str:
    amount = str(amount_in_cents)

    if len(amount) == 1:
        amount = "0,0" + amount
    elif len(amount) == 2:
        amount = "0," + amount
    else:
        digits = list(amount)
        digits.insert(-2, ",")
        amount = "".join(digits)

    return amount + " €"


async def sync_database(soure_database_file: Path, target_database_file: Path) -> None:
    if not soure_database_file.is_file():
        raise FileNotFoundError(f"File not found '{soure_database_file}'")

    if not target_database_file.is_dir():
        raise NotADirectoryError(f"Directory not found '{soure_database_file}'")

    async with in_syncing_lock:
        while True:
            try:
                async with async_open(soure_database_file, "rb") as src, async_open(
                    target_database_file / globals.DATABASE_FILE, "wb"
                ) as dest:
                    async for chunk in src.iter_chunked(65535):
                        await dest.write(chunk)

                print("Database synced.")
                break
            except Exception as e:
                secs = 60
                print("Failed sync.\n")
                print(e)
                print(f"\nRetry in {secs} sec...")

                await asyncio.sleep(secs)


def get_app_version() -> str:
    with open(
        Path(globals.WORKING_DIR) / "pyproject.toml", encoding="utf8", mode="r"
    ) as file:
        pyproject_file = toml.load(file)

    app_version = pyproject_file["tool"]["poetry"]["version"]

    if not app_version:
        raise ValueError("Could not read version from pyproject.toml")

    return app_version


def get_app_major_version() -> str:
    return get_app_version().split(".")[0]


# setlocale and decimal point for de_DE (. -> ,)
# does not work. This helper function shall be used untilthat problem is fixed
def cents_to_euro(amount_in_cent: int) -> str:
    return f"{amount_in_cent / 100:.2f} €".replace(".", ",")
