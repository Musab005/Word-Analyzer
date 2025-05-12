# Extract most significant words from a pdf using tf-idf

## To run:
`python -m scripts.extract_tfidf --pdf data\pdf_files\{filename.pdf} --stopwords data/stop_words_english.txt --output data/out_files/{filename.txt}`
from root

`python -m scripts.extract_top_20 --inputdir data\out_files --output data\out_files\{filename.json}`
from root