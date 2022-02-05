# The Application: Expenses Logger
The Expenses Logger tracks all expenses of a known list of users (list 'USERS' in globals.py)

When the list of users changes, all previous entries in the database will be deleted
and a new database will be created with current userlist from globals.py.

# Git
## Commit Cenvention
Proposed Commit Message Conventions:

- feat: for a new feature for the user, not a new feature for build script. Such commit will trigger a release bumping a MINOR version.
- fix: for a bug fix for the user, not a fix to a build script. Such commit will trigger a release bumping a PATCH version.
- perf: for performance improvements. Such commit will trigger a release bumping a PATCH version.
- docs: for changes to the documentation.
- style: for formatting changes, missing semicolons, etc.
- refactor: for refactoring production code, e.g. renaming a variable.
- test: for adding missing tests, refactoring tests; no production code change.
- build: for updating build configuration, development tools or other changes irrelevant to the user.
- wip: current state of branch may not work and is on "work in progress"

Based on: http://karma-runner.github.io/6.3/dev/git-commit-msg.html#allowed-type-values


# Database
## Alembic
### Datebase Migration
#### Create New Migration
alembic revision --autogenerate -m "MIGRATION NAME"

#### Update Migration to head
alembic update head

#### Downgrade Migration to specific migration
alembic downgrade MIGRATION_HASH

## Database App-Compatibilites
Please adjust after every version change!

| Database Version  | App Version |
| :---: | :---: |
| v0.X  | v0.X - current version (v0.1.0)  |

## Generate UI-Class from .ui-File
C:\Users\twitch\AppData\Local\pypoetry\Cache\virtualenvs\expenses-logger-q0tIoH39-py3.9\Scripts\pyside6-uic.exe file.ui > ui_file.py

### Converting problems:
- Problem: 🗑 will be converted as '\u1F5D1', which is too long for Python unicode escaping
- Solution: Replace '\u1F5D1' -> \U0001F5D1


- Problem: in Windows, pyside6-uic.exe creates non-utf-8 ui_xxx.py files. MyPy will get problems with non-utf-8 encoded .py files.
- Solution 1: convert ui file to UTF-8 (e.g. with notepad++) and save/replace ui_xxx.py file
- Solution 2: (suggestion from the community) maybe the environment variable 'PYTHONIOENCODING=utf8' could resolve that problem