import argparse

from src.merge_outputs import combine_tfidf, write_to_output


def main():
    parser = argparse.ArgumentParser(description="Combine TF-IDF results of all output*.txt files")
    parser.add_argument('--inputdir', type=str, default='data/out_files', help="Directory containing all pdf files")
    parser.add_argument('--output', type=str, default='data/out_files/tfidf_combined.json', help="Output json file path")

    args = parser.parse_args()

    tfidf_map = combine_tfidf(args.inputdir)
    write_to_output(tfidf_map, args.output)

    print(f"TF-IDF scores written to {args.output}")


if __name__ == '__main__':
    main()
