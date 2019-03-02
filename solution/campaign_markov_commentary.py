# BUG: make sure you're importing the right thing

import argv
from random import choice


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    chains = {}

    words = corpus.split()

    # BUG: index error
    for i in range(len(words) - 1):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        # BUG: add is not the correct method for this data type
        chains[key].add(value)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    chain_keys = chains.keys()
    key = chain_keys[0]
    words = [key[0], key[1]]
    count = 0

    # BUG: count will never be greater than 140
    while key in chains and count > 140:

        word = choice(chains[key])
        count += len(word)
        words.append(word)
        key = (key[1], word)

    return " ".join(words)


input_path = sys.argv[1]
input_text = open(input_path).read()

# BUG: calling the wrong input variable
chains = make_chains(input_path)

random_text = make_text(chains)

print random_text
