#!/bin/sh
source env/Scripts/activate #If running in unix based OS use: 'source env/bin/activate' instead
kaggle datasets download -d patricklford/bible-and-quran-sentiment-analysis -p data
unzip data/bible-and-quran-sentiment-analysis.zip -d data/
rm data/bible-and-quran-sentiment-analysis.zip