import argparse
from pathlib import Path

from src.pdf_utils import extract_text_from_pdf
from src.text_processing import read_stop_words, compute_tfidf, write_tfidf_scores


def main():
    parser = argparse.ArgumentParser(description="Extract TF-IDF from a PDF file.")
    parser.add_argument('--pdf', type=str, required=True, help="Path to input PDF file")
    parser.add_argument('--stopwords', type=str, required=True, help="Path to stop_words.txt")
    parser.add_argument('--output', type=str, default='data/tfidf_output.txt', help="Output file path")

    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    stop_words_path = Path(args.stopwords)
    output_path = Path(args.output)

    stop_words = read_stop_words(stop_words_path)
    documents = extract_text_from_pdf(pdf_path)
    tfidf_scores = compute_tfidf(documents, stop_words)
    write_tfidf_scores(output_path, tfidf_scores)

    print(f"TF-IDF scores written to {output_path}")


if __name__ == "__main__":
    main()
