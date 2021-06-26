import pandas as pd

from app import cache
from utils.constants import TIMEOUT
import pathlib
# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../data").resolve()


@cache.memoize(timeout=TIMEOUT)
def query_data():
    # This could be an expensive data querying step
    data_skripsi = pd.read_csv(DATA_PATH.joinpath('judul_skripsi.csv'), sep=';')
    return data_skripsi.to_json(date_format='iso', orient='split')


def query_dataframe():
    return pd.read_json(query_data(), orient='split')