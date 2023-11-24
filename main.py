# coding=utf-8

"""
Codi per executar tots els exercicis
"""

from src import (
    Exercici1_1, Exercici1_2, Exercici2_1, Exercici2_2, Exercici3,
    Exercici4_1, Exercici4_2, Exercici5, Exercici6, Exercici7
)
ZIP_FILE_PATH = "data/twitter_reduced.zip"
CSV_PROCESSED_PATH = "./data/twitter_processed.csv"
EXTRACT_FOLDER = "data"

"""Processa els arguments per determinar quins exercicis s'ha d'executar"""
def main():
    # Exercici 1.1
    """Executa l'exercici 1.1"""

    print("""Executa l'exercici 1.1""")
    Exercici1_1.import_csv_from_zip(ZIP_FILE_PATH, EXTRACT_FOLDER)

    # Exercici 1.2
    """Executa l'exercici 1.2"""

    print("""Executa l'exercici 1.2""")
    dataset = Exercici1_2.read_csv_to_dataframe('data/twitter_reduced.csv')
    dataframe = dataset

    # Exercici 2.1
    """Executa l'exercici 2.1"""

    print("""Executa l'exercici 2.1""")
    dataframe = Exercici2_1.preprocess_dataframe(dataframe)

    # Exercici 2.2
    """Executa l'exercici 2.2"""

    print("""Executa l'exercici 2.2""")
    Exercici2_2.remove_stop_words(dataframe)

    # Exercici 3
    """Executa l'exercici 3"""

    print("""Executa l'exercici 3""")
    frequencies = Exercici3.process_words(dataframe)

    # Exercici 4.1
    """Executa l'exercici 4.1"""

    print("""Executa l'exercici 4.1""")
    dataset = Exercici4_1.append_frequencies(dataset, frequencies)

    # Exercici 4.2
    """Executa l'exercici 4.2"""

    print("""Executa l'exercici 4.2""")
    Exercici4_2.save_process_dataset(dataset, CSV_PROCESSED_PATH)

    # Exercici 5
    """Executa l'exercici 5"""

    print("""Executa l'exercici 5""")
    Exercici5.get_wordcloud()

    # Exercici 6
    """Executa l'exercici 6"""

    print("""Executa l'exercici 6""")
    Exercici6.generate_histogram(dataframe)

    # Exercici 7
    """Executa l'exercici 7"""

    print("""Executa l'exercici 7""")
    Exercici7.preguntes()

if __name__ == "__main__":
    main()