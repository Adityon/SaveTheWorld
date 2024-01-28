import time
import random

class Player:
    def __init__(self, name, password):
        self.name = name
        self.points = 0
        self.word_score = 0
        self.level = 1
        self.password = password

    def add_points(self, point):
        self.points += point
        self.word_score += point

    def level_up(self):
        self.level += 1
        print(f"Congratulations! You've advanced to Level {self.level}")

    def __str__(self):
        return f"Player {self.name}, Level {self.level}, Points {self.points}, Word Score {self.word_score}"

word_list = [
    'aardvark', 'aardwolf', 'aaron', 'aback', 'abacus', 'abaft', 'abalone', 'abandon', 'abandoned', 'abandonment',
    'abandons', 'abase', 'abased', 'abasement', 'abash', 'abashed', 'abate', 'abated', 'abatement', 'abates',
    'abattoir', 'abattoirs', 'abbe', 'abbess', 'abbey', 'abbeys', 'abbot', 'abbots', 'abbreviate', 'abbreviated',
    'abbreviates', 'abbreviating', 'abbreviation', 'abbreviations', 'abdicate', 'abdicated', 'abdicates', 'abdicating',
    'abdication', 'abdomen', 'abdomens', 'abdominal', 'abduct', 'abducted', 'abducting', 'abduction', 'abductions',
    'abductor', 'abductors', 'abducts', 'abe', 'abeam', 'abel', 'abele', 'aberdeen', 'aberrant', 'aberration',
    'aberrations', 'abet', 'abets', 'abetted', 'abetting', 'abeyance', 'abhor', 'abhorred', 'abhorrence', 'abhorrent',
    'abhors', 'abide', 'abided', 'abides', 'abiding', 'abidjan', 'abies', 'abilities', 'ability', 'abject', 'abjectly',
    'abjure', 'abjured', 'ablate', 'ablates', 'ablating', 'ablation', 'ablative', 'ablaze', 'able', 'ablebodied', 'abler',
    'ablest', 'abloom', 'ablution', 'ablutions', 'ably', 'abnegation', 'abnormal', 'abnormalities', 'abnormality',
    'abnormally', 'aboard', 'abode', 'abodes', 'abolish', 'abolished', 'abolishes', 'abolishing', 'abolition',
    'abolitionist', 'abolitionists', 'abomb', 'abominable', 'abominably', 'abominate', 'abominated', 'abomination',
    'abominations', 'aboriginal', 'aborigines', 'abort', 'aborted', 'aborting', 'abortion', 'abortionist',
    'abortionists', 'abortions', 'abortive', 'aborts', 'abound', 'abounded', 'abounding', 'abounds', 'about', 'above',
    'abraded', 'abraham', 'abrasion', 'abrasions', 'abrasive', 'abrasively', 'abrasiveness', 'abrasives', 'abreast',
    'abridge', 'abridged', 'abridgement', 'abridging', 'abroad', 'abrogate', 'abrogated', 'abrogating', 'abrogation',
    'abrogations', 'abrupt', 'abruptly', 'abruptness', 'abscess', 'abscesses', 'abscissa', 'abscissae', 'abscissas',
    'abscond', 'absconded', 'absconder', 'absconding', 'absconds', 'abseil', 'abseiled', 'abseiler', 'abseiling', 'abseils',
    'absence', 'absences', 'absent', 'absented', 'absentee', 'absenteeism', 'absentees', 'absenting', 'absently',
    'absentminded', 'absentmindedly', 'absentmindedness', 'absolute', 'absolutely', 'absoluteness', 'absolutes',
    'absolution', 'absolutism', 'absolutist', 'absolutists', 'absolve', 'absolved', 'absolves', 'absolving', 'absorb',
    'absorbed', 'absorbency', 'absorbent', 'absorber',
    'absorbing', 'absorbingly', 'absorbs', 'absorption', 'absorptions', 'absorptive', 'absorptivity', 'abstain', 'abstained',
    'abstainer', 'abstainers', 'abstaining', 'abstains', 'abstemious', 'abstemiously', 'abstemiousness', 'abstention',
    'abstentions', 'abstinence', 'abstinent', 'abstract', 'abstracted', 'abstractedly', 'abstracting', 'abstraction',
    'abstractions', 'abstractly', 'abstracts', 'abstruse', 'abstrusely', 'absurd', 'absurder', 'absurdest', 'absurdist',
    'absurdities', 'absurdity', 'absurdly', 'abundance', 'abundances', 'abundant', 'abundantly', 'abuse', 'abused',
    'abuser', 'abusers', 'abuses', 'abusing', 'abusive', 'abusively', 'abusiveness', 'abut', 'abutment', 'abutments',
    'abutted', 'abutting', 'abuzz', 'aby', 'abs',     'abuzz', 'aby', 'abysmal', 'abysmally', 'abyss', 'abyssal', 'abysses', 'acacia', 'academe',
    'academia', 'academic', 'academical', 'academically', 'academician', 'academicians', 'academics', 'academies',
    'academy', 'acanthus', 'acapulco', 'accede', 'acceded', 'acceding', 'accelerate', 'accelerated', 'accelerates',
    'accelerating', 'acceleration', 'accelerations', 'accelerator', 'accelerators', 'accelerometer', 'accelerometers',
    'accent', 'accented', 'accenting', 'accents', 'accentuate', 'accentuated', 'accentuates', 'accentuating',
    'accentuation', 'accept', 'acceptability', 'acceptable', 'acceptably', 'acceptance', 'acceptances', 'accepted',
    'accepting', 'acceptor', 'acceptors', 'accepts', 'access', 'accessed', 'accesses', 'accessibility', 'accessible',
    'accessing', 'accession', 'accessions', 'accessories', 'accessory', 'accidence', 'accident', 'accidental',
    'accidentally', 'accidentprone', 'accidents', 'acclaim', 'acclaimed', 'acclaims', 'acclamation', 'acclamations',
    'acclimatisation', 'acclimatise', 'acclimatised', 'acclimatising', 'accolade', 'accolades', 'accommodate',
    'accommodated', 'accommodates', 'accommodating', 'accommodation', 'accommodations', 'accompanied', 'accompanies',
    'accompaniment', 'accompaniments', 'accompanist', 'accompany', 'accompanying', 'accomplice', 'accomplices',
    'accomplish', 'accomplished', 'accomplishes', 'accomplishing', 'accomplishment', 'accomplishments', 'accord',
    'accordance', 'accorded', 'according', 'accordingly', 'accordion', 'accordionist', 'accordions', 'accords',
    'accost', 'accosted', 'accosting', 'accosts', 'account', 'accountability', 'accountable', 'accountancy', 'accountant',
    'accountants', 'accounted', 'accounting', 'accounts', 'accra', 'accredit', 'accreditation', 'accredited', 'accrediting',
    'accredits', 'accreted', 'accretion', 'accretions', 'accrual', 'accruals', 'accrue', 'accrued', 'accrues', 'accruing',
    'accumulate', 'accumulated', 'accumulates', 'accumulating', 'accumulation', 'accumulations'
]

character_already_registered = {}

# condition for registration and login
chance = int(input("How many times do you wanna play? "))
name = input("What is your name? ")
password = input("What is your password? ")

while chance > 0:
    print("You have " + str(chance) + " chances left")

    if name not in character_already_registered:
        new_player = Player(name, password)
        character_already_registered[name] = new_player

    else:
        print("Use a new username; this is already taken")
    
    current_player = character_already_registered[name]
    print(current_player)
    time.sleep(1)
    print("Start Guessing...")
    time.sleep(0.5)

    word = random.choice(word_list)
    guesses = ""
    turns = 6

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end="")
            else:
                print("_", end="")
                failed += 1
        if failed == 0:
            print("\nYou Won")
            new_player.add_points(10)
            new_player.level_up()  # Level up after each correctly guessed word
            break
        guess = input("\nGuess a character: ")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("You have", turns, 'more guesses')
        if turns == 0:
            print("You Lose")
            chance = chance - 1

# Print the final player information after the game
print(current_player)