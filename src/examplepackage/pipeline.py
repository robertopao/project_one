"""
This module should contain your main project pipeline(s).

Whilst the pipeline may change during the analysis phases, any more stable pipeline should be implemented here so
that it can be reused and easily reproduced.
"""
import pandas as pd

from examplepackage import features
from examplepackage.i_o import IO
from examplepackage.examplemodule import  hello_world


def run_pipeline(local_data_path: object) -> object:
    """
    Run the main processing pipeline.

    Returns:
        A dataframe containing the output of the pipeline
    """

    # io = IO(path)
    # df = io.load_cleaned_file(download_always=False)
    # df = add_choke_events(df)

    # Add calls to features.Xxx here
    string_to_print=hello_world()
    print(string_to_print)



    # save (or return) dataframe here?
    return string_to_print


okkkk=run_pipeline('/home/visionlab/Desktop/dati')