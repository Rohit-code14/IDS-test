# with open("git_payload.txt", "r") as infile, open("xss_payload.txt", "w") as outfile:
#     # Read all lines from input file
#     lines = infile.readlines()
#     num_lines = len(lines)

#     # Duplicate lines to reach 10000 if necessary
#     if num_lines < 10000:
#         num_duplicates = 10000 - num_lines
#         for i in range(num_duplicates):
#             lines.append(lines[i % num_lines])

#     # Write lines to output file
#     outfile.writelines(lines[:10000])

# import random
# import string

# with open("words.txt", "w") as outfile:
#     for i in range(10000):
#         # Generate random number to decide on word count
#         num_words = random.randint(1, 2)

#         # Generate words using string module
#         words = ["".join(random.choices(string.ascii_letters, k=random.randint(4, 10))) for _ in range(num_words)]

#         # Join words with space delimiter
#         text = " ".join(words)

#         # Write text to output file
#         outfile.write(text + "\n")

import nltk
from faker import Faker
import random

nltk.download('wordnet')

fake = Faker()

def generate_nouns(num):
    nouns = set()
    while len(nouns) < num:
        nouns.add(fake.word().lower())
    return list(nouns)

def generate_verbs(num):
    verbs = set()
    while len(verbs) < num:
        verb = fake.word().lower()
        if nltk.corpus.wordnet.synsets(verb, pos='v'):
            verbs.add(verb)
    return list(verbs)

def generate_tourist_places(num):
    places = set()
    while len(places) < num:
        places.add(fake.city().lower())
    return list(places)

def generate_emails(num):
    emails = set()
    while len(emails) < num:
        emails.add(fake.email().lower())
    return list(emails)

def generate_names(num):
    names = set()
    while len(names) < num:
        names.add(fake.name().lower())
    return list(names)

nouns = generate_nouns(5000)
verbs = generate_verbs(2500)
tourist_places = generate_tourist_places(1500)
emails = generate_emails(500)
names = generate_names(500)

random_words = random.sample(nouns + verbs + tourist_places + emails + names, 10000)

with open('random_strings.txt', 'w') as f:
    for word in random_words:
        f.write(word + '\n')

