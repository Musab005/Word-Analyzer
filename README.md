# Extract most significant words from a pdf using tf-idf

## To extract tfidf results from a single pdf file:
`python -m scripts.extract_tfidf --pdf data\pdf_files\{filename.pdf} --stopwords data/stop_words_english.txt --output data/out_files/{filename.txt}`
from root

## To combine tfidf results of all output*.txt files in the data\out_files directory
`python -m scripts.extract_top_20 --inputdir data\out_files --output data\out_files\{filename.json}`
from root