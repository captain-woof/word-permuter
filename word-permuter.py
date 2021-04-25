#!/usr/bin/python3

from argparse import ArgumentParser
from time import sleep

base_words = []
base_words_length = None

class Sequencer:
    def __init__(self, n):
        self.sequence = []
        self.carry = None
        for _ in range(0, n-1):
            self.sequence.append(0)
        self.sequence.append(-1)
        self.sequence_len = len(self.sequence)

    def __inc(self):
        # Increment sequence
        self.carry = False
        self.sequence[-1] += 1

        # Check for end of sequence
        check = 0
        for seq in self.sequence:
            check += seq
        if check > (self.sequence_len * (base_words_length - 1)):
            return False

        # Resolve carrys
        for i in range(1, self.sequence_len + 1):
            if self.carry:
                self.sequence[-i] += 1
                self.carry = False
            if self.sequence[-i] == base_words_length:
                self.sequence[-i] = 0
                self.carry = True

        return True

    def next(self):
        stat = self.__inc()
        if not stat:
            return None
        else:
            return tuple(self.sequence)

# MAIN CODE
if __name__ == '__main__':
    description = "Produces all (length) permutations of words provided in a wordlist(s); very useful for generating base passwords for specfic target users from common passwords (like the user's information). Password wordlist example: Prepare a basic wordlist of the target user's information like pet name, first school, etc, then pass the list to this tool, and it will produce all possible permuations of the words from taking 1 at a time (changeable) to taking all at a time (also changeable)."
    epilogue = "Written by CaptainWoof"

    parser = ArgumentParser(description=description, epilog=epilogue)
    parser.add_argument("-f", "--file", action="append", required=True, type=str,
                        help="Text file to read base words from; can be used multiple times.")
    parser.add_argument("-m", "--minwords", action="store", required=False, type=int, default=1,
                        help="Minimum number of base words to produce permuations with; default=1")
    parser.add_argument("-M", "--maxwords", action="store", default=-1, required=False, type=int,
                        help="Maximum number of base words to produce permuations with; default=maximum")
    parser.add_argument("-o", "--output", action="store", required=False, type=str,
                        help="Output file to store the permuations in.")
    args = parser.parse_args()

    # READY ARGS
    files_to_read = args.file
    if args.output is not None:
        output = open(args.output, 'w+')
    else:
        output = None
    min_words = args.minwords
    max_words = args.maxwords

    # GET ALL BASE WORDS
    for file in files_to_read:
        with open(file, 'r') as f:
            for word in f.readlines():
                base_words.append(word.strip())
    # Check
    if len(base_words) == 0:
        print("Could not find any input base words !")
        exit(0)
    else:
        base_words_length = len(base_words)
    if max_words == -1:
        max_words = len(base_words)

    total_permutations = 0
    average_wordlength = 0
    filesize = 0
    for word in base_words:
    	average_wordlength += len(word) / base_words_length
    for n in range(min_words,max_words+1):
    	total_permutations += base_words_length ** n
    	filesize += total_permutations * n * average_wordlength
    
    # START PERMUTING
    print("Total base words: {}".format(len(base_words)))
    print("Total permuations to be produced: {}".format(total_permutations))
    print("Predicted size of outout (will vary): {} bytes, {:.2f} KB, {:.2f} MB, {:.2f} GB".format(filesize,filesize/1024,filesize/(1024**2),filesize/(1024**3)))
    print("Will start in 3 seconds...")
    try:
        sleep(3)
    except KeyboardInterrupt:
        print("Interrupted !")
        exit(0)
    print("\nWORDLIST\n--------")

    for n in range(min_words, max_words + 1):
        sequencer = Sequencer(n)
        sequence = sequencer.next()
        while sequence is not None:
            combination = ""
            for i in sequence:
                combination += base_words[i]
            if output is not None:
                output.write(combination + '\n')
            print(combination)
            sequence = sequencer.next()

    # Close file
    if output is not None:
        output.close()