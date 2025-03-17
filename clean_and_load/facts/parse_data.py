from typing import List
import pandas as pd
from io import StringIO
import os


def to_csv_file(dataframe: pd.DataFrame, path: str, filename: str):
    dataframe.to_csv(os.path.join(path, f"{filename}.csv"), index=False)


def parse_and_combine(responses: List[str], columns_to_drop: List[str] = []):
    """
    Receives a list of stringified csv responses and optionally a number of column to drop and returns a dataframe
    """

    main_df = pd.DataFrame()

    for response in responses:
        if response != None:
            main_df = pd.concat(
                [main_df, pd.read_csv(StringIO(response), dtype="str")],
                ignore_index=True,
            )

    main_df.drop(columns=columns_to_drop, inplace=True)
    return main_df
