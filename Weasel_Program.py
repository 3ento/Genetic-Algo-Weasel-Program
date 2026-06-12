from random import randint, choice

# constants
TARGET_PHRASE = "methinks it is like a weasel"
LEGAL_CHARACTERS = "abcdefghijklmnopqrstuvwxyz "
POPULATION_SIZE = 100000
MUTATION_CHANCE = 100000 # or 10^-5, the mutation chance of a gene in viruses
TARGET_PHRASE_LENGTH = len(TARGET_PHRASE)
LEGAL_CHARACTERS_COUNT = len(LEGAL_CHARACTERS)

# Hamming distance pairs up the letters in a word and sums up all the differences, so a lower score
# shows the phrase is getting closer to the target
def hamming_distance(phrase):
    return sum(target_character != phrase_character for target_character, phrase_character in zip(TARGET_PHRASE, phrase))

# Simulate cell division, where each character represents a gene, each with a certain
# chance to mutate
def reproduce(phrase):
    return [
        choice(LEGAL_CHARACTERS)
        if randint(1, MUTATION_CHANCE) == 1 else c
        for c in phrase
    ]

current_phrase = [choice(LEGAL_CHARACTERS)
                  for i in range(TARGET_PHRASE_LENGTH)
                  ]
current_best_distance = hamming_distance(current_phrase)
generation_count = 0

print(f"Starting string: {''.join(current_phrase)}")

# Run a loop to simulate each child in the population reproducing
# and taking the best, closest one. Then the population is doubled to
# simulate an actual increase in numbers
while current_best_distance > 0:
    generation_count += 1

    fittest_offspring = min(
        (reproduce(current_phrase)
         for _ in range(POPULATION_SIZE)),
        key=hamming_distance
    )

    fittest_offspring_distance = hamming_distance(fittest_offspring)

    if fittest_offspring_distance < current_best_distance:
        current_best_distance = fittest_offspring_distance
        current_phrase = fittest_offspring

        print(f"Gen {generation_count}:", end='')
        for c1, c2 in zip(current_phrase, TARGET_PHRASE):
            if c1 == c2:
                print(f"\x1b[107m\x1b[30m{c1}\x1b[0m\x1b[0m", end='')
            else:
                print(c1, end='')
        print()