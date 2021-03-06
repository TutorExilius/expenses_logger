from datetime import datetime
from typing import Dict, List

from expenses_logger import globals
from expenses_logger.model.models import Entry, User
from sqlalchemy import create_engine
from sqlalchemy.orm import load_only, sessionmaker

engine = create_engine(globals.DATABASE_URL)
Session = sessionmaker(engine)


def initialize_new_database() -> None:
    print("Create new database...")
    initialize_new_users(globals.USERS)
    print("Database created:", globals.DATABASE_URL)


def get_user_amounts() -> Dict[str, int]:
    selected_year = datetime.utcnow().year
    current_user_amount_map = {
        user_name: get_total_amount_in_cents(user_name, selected_year)
        for user_name in get_user_names()
    }

    oldest_year = get_oldest_year()
    last_years_total_user_amount_map = {user_name: 0 for user_name in get_user_names()}

    for year in range(oldest_year, selected_year):
        for user_name in current_user_amount_map.keys():
            last_years_total_user_amount_map[user_name] += get_total_amount_in_cents(
                user_name, year
            )

    minimum_amount = min(last_years_total_user_amount_map.values())
    for user_name in current_user_amount_map.keys():
        last_years_total_user_amount_map[user_name] -= minimum_amount

    for user_name in current_user_amount_map.keys():
        current_user_amount_map[user_name] += last_years_total_user_amount_map[
            user_name
        ]

    return current_user_amount_map


def empty_database() -> None:
    print("Empty Database...")

    delete_all_users()
    print("Note: all entries of users will be deleted (cascade delete).")

    print("Database emptied.")


def delete_all_users() -> None:
    with Session() as session:
        for user in session.query(User).all():
            print(f"Delete '{user.user_name}' ...")
            session.delete(user)
            print(f"'{user.user_name}' deleted.")

        session.commit()


def initialize_new_users(user_names: List[str]) -> None:
    with Session() as session:
        print("Create new users...")

        for user_name in user_names:
            user = User(user_name=user_name, created_at=datetime.utcnow())
            session.add(user)
            print(f"Created '{user_name}' in users table.")

        session.commit()
        print("Finished User Creation.")


def add_amount(user_name: str, amount_in_cents: int) -> None:
    with Session() as session:
        user = session.query(User).filter_by(user_name=user_name).one_or_none()

        if user is None:
            raise ValueError(
                f"Can't update amount for user '{user_name}', User not found."
            )

        entry = Entry(amount_in_cents=amount_in_cents, created_at=datetime.utcnow())
        user.entries.append(entry)

        print(f"Added '{amount_in_cents}' for user '{user_name}'.")

        session.commit()


def get_total_amount_in_cents(user_name: str, year: int) -> int:
    with Session() as session:
        user = session.query(User).filter_by(user_name=user_name).one_or_none()

        if user is None:
            raise ValueError(
                f"Can't update amount for user '{user_name}', User not found."
            )

        entry_amounts_in_year = (
            entry.amount_in_cents
            for entry in user.entries
            if entry.created_at.year == year
        )
        return sum(entry_amounts_in_year)


def get_oldest_year() -> int:
    with Session() as session:
        user_names = globals.USERS

        oldest_year = datetime.utcnow().year

        for user_name in user_names:
            user = session.query(User).filter_by(user_name=user_name).one_or_none()

            if user is None:
                raise ValueError(
                    f"Can't update amount for user '{user_name}', User not found."
                )

            if user.entries:
                user_entries = sorted(user.entries, key=lambda entry: entry.created_at)
                year = user_entries[0].created_at.year
                if oldest_year > year:
                    oldest_year = year

    return oldest_year


def get_user_names() -> List[str]:
    with Session() as session:
        users = session.query(User).options(load_only("user_name")).all()

    return [user.user_name for user in users]
