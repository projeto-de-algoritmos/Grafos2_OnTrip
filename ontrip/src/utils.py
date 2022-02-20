import pandas as pd


def read_csv(path: str, cols: list) -> None:
    """
    This function read the routes csv file and returns a list of tuple with
    the source airport and the destination airport
    :param path: Path to the csv file
    :returns List[tuple[str, str]]: A list of source and destination airports tuple
    """
    df = pd.read_csv(path, usecols=cols)
    return df.values.tolist()