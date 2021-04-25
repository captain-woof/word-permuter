# README

### Introduction

**word-permuter** produces all (length) permutations of words provided in a wordlist(s); very useful for generating base passwords for specfic target users from common
passwords (like the user's information). Password wordlist example: Prepare a
basic wordlist of the target user's information like pet name, first school,
etc, then pass the list to this tool, and it will produce all possible
permuations of the words from taking 1 at a time (changeable) to taking all at
a time (also changeable).

### Usage

```
optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Text file to read base words from; can be used
                        multiple times.
  -m MINWORDS, --minwords MINWORDS
                        Minimum number of base words to produce combinations
                        with; default=1
  -M MAXWORDS, --maxwords MAXWORDS
                        Maximum number of base words to produce combinations
                        with; default=maximum
  -o OUTPUT, --output OUTPUT
                        Output file to store the combinations in.
```

### Example

**Using a demo file:**

*test.txt*
```
saint
john
ricky
```

**Output:**
```
WORDLIST
--------
saint
john
ricky
saintsaint
saintjohn
saintricky
johnsaint
johnjohn
johnricky
rickysaint
rickyjohn
rickyricky
saintsaintsaint
saintsaintjohn
saintsaintricky
saintjohnsaint
saintjohnjohn
saintjohnricky
saintrickysaint
saintrickyjohn
saintrickyricky
johnsaintsaint
johnsaintjohn
johnsaintricky
johnjohnsaint
johnjohnjohn
johnjohnricky
johnrickysaint
johnrickyjohn
johnrickyricky
rickysaintsaint
rickysaintjohn
rickysaintricky
rickyjohnsaint
rickyjohnjohn
rickyjohnricky
rickyrickysaint
rickyrickyjohn
rickyrickyricky
```

### Author

**[@realCaptainWoof](https://twitter.com/realCaptainWoof)**

