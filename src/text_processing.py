from sklearn.feature_extraction.text import TfidfVectorizer
import re


def read_stop_words(stop_words_path):
    with open(stop_words_path, "r", encoding="utf-8") as f:
        raw_words = f.read().splitlines()
    pattern = re.compile(r"\b\w\w+\b", flags=re.UNICODE)
    return [word for word in raw_words if pattern.fullmatch(word)]


def compute_tfidf(documents, stop_words):
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]
    return sorted(zip(feature_names, scores), key=lambda x: x[1], reverse=True)


def write_tfidf_scores(output_path, tfidf_scores):
    with open(output_path, 'w', encoding='utf-8') as out:
        for word, score in tfidf_scores:
            out.write(f"{word}: {score:.4f}\n")
