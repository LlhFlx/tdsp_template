from pathlib import Path
import sys
import spacy
import time
import re
import pandas as pd
import numpy as np

# Add parent directory to path to import from data_acquisition
PARENT_DIR = str(Path(__file__).parent.parent)
sys.path.append(PARENT_DIR)
from data_acquisition.main import load_religious_texts
from gensim.models.word2vec import Word2Vec
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text.lower())
    processed_text = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(processed_text).strip()
def split_verses(text):
    #pattern = r'\d+:\d+'
    pattern = r'\b\d+:\d+\b'
    verses = re.split(f'({pattern})', text)
    verses = [verses[i] + verses[i+1] for i in range(1, len(verses)-1, 2)]
    return verses

def delete_numbers(doc):
    pattern = r'\d+:\d+'  # Para eliminar solo números en formato XX:YY
    # Sustituimos las coincidencias por una cadena vacía
    result = re.sub(pattern, '', doc)
    return result.strip()  # Eliminar espacios extra al inicio o final si quedan

def clean(old_testament):
    old_testament.rename(columns={"The Old Testament of the King James Version of the Bible": "verse"}, inplace=True)
    old_testament['cleaned_verses'] = old_testament['verse'].apply(preprocess_text)
    old_testament['cleaned_verses'] = old_testament['cleaned_verses'].apply(lambda x: ' '.join(x.split()))
    old_testament['cleaned_verses'] = old_testament['cleaned_verses'].fillna("").apply(delete_numbers)
    old_testament = old_testament.drop_duplicates()
    return old_testament

def get_clean_data():
    output_path = Path('./data/clean_old_testament.csv')
    
    if output_path.exists():
        print(f"Cleaned data already exists at {output_path}. Skipping loading and cleaning.")
        data = pd.read_csv(output_path)
    else:
        try:
            print("Loading religious texts...")
            start_loading = time.time()
            _, old_testament = load_religious_texts()
            end_loading = time.time()
            print(f"Time taken to load the data: {end_loading - start_loading:.2f} seconds")
            
            print("Start cleaning...")
            start_cleaning = time.time()
            data = clean(old_testament)
            print("Cleaning Finished!")
            end_cleaning = time.time()
            print(f"Time taken to clean the data: {end_cleaning - start_cleaning:.2f} seconds")
            
            # Save the cleaned DataFrame to a CSV
            output_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
            data.to_csv(output_path, index=False)
            print(f"Cleaned data saved to {output_path}")
            
        except Exception as e:
            print(f"An error occurred during cleaing: {str(e)}")
            sys.exit(1)
    return data


def feature_extraction(tokens):
    return Word2Vec(
            sentences = tokens,
            vector_size = 100,
            epochs = 20,
            workers = -1 # específica que se debe usar el número máximo de procesos.
            )

def main() -> None:
    """Main function to perform data cleaning."""
    
    data = get_clean_data()
    # Show a random row
    random_row = data.sample(n=1).iloc[0]
    print("\nRandom row comparison:")
    print(f"**Original Verse: {random_row['verse']}")
    print(f"**Cleaned Verse: {random_row['cleaned_verses']}")
    print("---")
    try:
        tokens = list(map(lambda doc: str(doc).split(" "), data['cleaned_verses']))
        embedding = feature_extraction(tokens)
        print("type", type(embedding.wv))
        embedding_model = {word: embedding.wv[word] for word in embedding.wv.index_to_key}
        np.savez_compressed('./models/embeddings_bible.npz', **embedding_model) #save embeding in a file
        vect = embedding.wv[tokens[10]]
        print("Ejemplo del embedding")
        print(tokens[10])
        print(vect)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
