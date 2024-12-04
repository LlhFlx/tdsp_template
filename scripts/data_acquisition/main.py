import pandas as pd
import os
from typing import Tuple

# Define constants
DATA_PATH = 'data/'
QURAN_FILENAME = 'Quran_english.csv'
OLD_TESTAMENT_FILENAME = 'Old_Testament_KJ_Bible.csv'

def load_religious_texts(data_path: str = DATA_PATH) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load religious texts data from CSV files.
    
    Args:
        data_path (str): Path to the directory containing the data files
        
    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: Tuple containing Quran and Old Testament dataframes
    """
    try:
        quran = pd.read_csv(os.path.join(data_path, QURAN_FILENAME))
        old_testament = pd.read_csv(os.path.join(data_path, OLD_TESTAMENT_FILENAME))
        return quran, old_testament
    except FileNotFoundError as e:
        print(f"Error loading data files: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error while loading data: {e}")
        raise

def main():
    """Main function to load and display religious texts data."""
    print(f"Script running directory: {os.getcwd()}")
    
    quran, old_testament = load_religious_texts()
    
    print("\nQuran [English]:")
    print(quran.head())
    
    print("\nOld Testament [English]:")
    print(old_testament.head())

if __name__ == "__main__":
    main()