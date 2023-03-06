import argparse

def combine_wordlists(w1, w2, output):
    with open(w1, 'r') as f1:
        words = set([w.strip() for w in f1.readlines()])

    with open(w2, 'r') as f2:
        words.update(set([w.strip() for w in f2.readlines()]))

    with open(output, 'w') as out_file:
        for word in sorted(words):
            out_file.write(word + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Combine two wordlists and write to a new file.')
    parser.add_argument('-w1', '--wordlist1', required=True, help='First wordlist file.')
    parser.add_argument('-w2', '--wordlist2', required=True, help='Second wordlist file.')
    parser.add_argument('-o', '--output', required=True, help='Output file name.')
    args = parser.parse_args()

    combine_wordlists(args.wordlist1, args.wordlist2, args.output)
