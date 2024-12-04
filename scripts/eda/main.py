"""
Exploratory Data Analysis (EDA) script for religious texts.

This module performs basic statistical analysis and text properties examination
on religious text datasets, focusing on the Old Testament corpus.
"""

import pandas as pd
import os
import sys
from pathlib import Path
from typing import Dict, Any

# Add parent directory to path to import from data_acquisition
PARENT_DIR = str(Path(__file__).parent.parent)
sys.path.append(PARENT_DIR)
from data_acquisition.main import load_religious_texts


def get_corpus_stats(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Calculate basic statistics about the text corpus.
    
    Args:
        df (pd.DataFrame): DataFrame containing the text corpus
        
    Returns:
        Dict[str, Any]: Dictionary containing corpus statistics including:
            - Number of rows
            - File size in MB
            - Count of null values per column
            - Presence of invalid characters
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
        
    stats = {
        'num_rows': len(df),
        'filesize_mb': df.memory_usage(deep=True).sum() / (1024 * 1024),
        'null_values': df.isnull().sum().to_dict(),
        'has_invalid_chars': df['verse'].str.contains(r'[^\x00-\x7F]').any()
    }
    return stats


def analyze_text_properties(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Analyze text properties of the verses.
    
    Args:
        df (pd.DataFrame): DataFrame containing the verses
        
    Returns:
        Dict[str, Any]: Dictionary containing text analysis results including:
            - Average, max, and min verse lengths
            - Average, max, and min word counts
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    if 'verse' not in df.columns:
        raise ValueError("DataFrame must contain a 'verse' column")
        
    df_copy = df.copy()
    df_copy['verse_length'] = df_copy['verse'].str.len()
    df_copy['word_count'] = df_copy['verse'].str.split().str.len()
    
    analysis = {
        'avg_verse_length': df_copy['verse_length'].mean(),
        'max_verse_length': df_copy['verse_length'].max(),
        'min_verse_length': df_copy['verse_length'].min(),
        'avg_word_count': df_copy['word_count'].mean(),
        'max_word_count': df_copy['word_count'].max(),
        'min_word_count': df_copy['word_count'].min()
    }
    return analysis


def print_analysis_results(stats: Dict[str, Any], text_analysis: Dict[str, Any]) -> None:
    """
    Print formatted analysis results.
    
    Args:
        stats (Dict[str, Any]): Corpus statistics from get_corpus_stats
        text_analysis (Dict[str, Any]): Text analysis results from analyze_text_properties
    """
    print("\nCorpus Statistics:")
    print(f"Number of verses: {stats['num_rows']:,}")
    print(f"File size: {stats['filesize_mb']:.2f} MB")
    print(f"Null values: {stats['null_values']}")
    print(f"Contains invalid characters: {stats['has_invalid_chars']}")
    
    print("\nText Analysis:")
    print(f"Average verse length: {text_analysis['avg_verse_length']:.1f} characters")
    print(f"Verse length range: {text_analysis['min_verse_length']:,} - {text_analysis['max_verse_length']:,} characters")
    print(f"Average word count: {text_analysis['avg_word_count']:.1f} words")
    print(f"Word count range: {text_analysis['min_word_count']} - {text_analysis['max_word_count']} words")


def main() -> None:
    """Main function to perform exploratory data analysis."""
    try:
        print("Loading religious texts...")
        quran, old_testament = load_religious_texts()
        
        old_testament['verse'] = old_testament['The Old Testament of the King James Version of the Bible']

        print("\nAnalyzing Old Testament corpus:")
        print(old_testament.describe())
        
        ot_stats = get_corpus_stats(old_testament)
        ot_analysis = analyze_text_properties(old_testament)
        
        print_analysis_results(ot_stats, ot_analysis)
        
        print("\nColumn Information:")
        print(old_testament.info())
        
        print("\nDescriptive Statistics:")
        print(old_testament.describe())
        
    except Exception as e:
        print(f"An error occurred during analysis: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
