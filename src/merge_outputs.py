import json
from pathlib import Path


def combine_tfidf(inputdir):
    tfidf_map = {}
    if not Path(inputdir).is_dir():
        raise NotADirectoryError(f"Input path '{inputdir}' is not a valid directory.")
    for file_path in Path(inputdir).iterdir():
        if file_path.suffix == ".txt":
            with open(file_path, 'r', encoding="utf-8") as f:
                for line in f.readlines():

                    keyword = line.split(':', 1)[0].strip()
                    score = line.split(':', 1)[1].strip()
                    if keyword not in tfidf_map:
                        tfidf_map[keyword] = score
                    else:
                        old_score = tfidf_map[keyword]
                        if score > old_score:
                            tfidf_map[keyword] = score
    return tfidf_map


def write_to_output(tfidf_map, out_path):
    with open(out_path, 'w') as f:
        sorted_tfidf = dict(sorted(tfidf_map.items(), key=lambda item: item[1], reverse=True))
        json.dump(sorted_tfidf, f, indent=4)
