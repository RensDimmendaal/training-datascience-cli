import fire
import numpy as np
import pandas as pd


def print_save_summary(input_fpath,output_fpath):
    """
    input_fpath:
    """
    df = pd.read_csv(input_fpath)
    summary = df.describe()
    summary.to_csv(output_fpath)
    print(np.round(summary,2))


if __name__ == '__main__':
    # Example usage from project root:
    # python ./fire_demo/in_out.py ./data/chickweight.csv ./output/summary.csv
    fire.Fire(print_save_summary)