import pathlib
import dotenv

# import os

# from pprint import pprint


def init_config():
    CURRENT_DIR = pathlib.Path(__file__).resolve().parent
    BASE_DIR = CURRENT_DIR.parent
    ENV_FILE_PATH = BASE_DIR / ".env"

    dotenv.read_dotenv(str(ENV_FILE_PATH))

    print("Load Config")

    # pprint(os.environ)