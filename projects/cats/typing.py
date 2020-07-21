"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    i = 0
    while i <= k:
        if k > len(paragraphs) - 1:
            return ''
        if select(paragraphs[i]) == False:
            k += 1
        i += 1
    return paragraphs[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(paragraph):
        for word in topic:
            if word in remove_punctuation(paragraph).lower().split():
                return True
        return False
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    accur,i = 0, 0
    while i < min(len(typed_words), len(reference_words)):
        if typed_words[i] == reference_words[i]:
            accur += 1
        i += 1
    if accur == 0:
        return 0.0
    else:
        return accur / len(typed_words) * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 / elapsed * 60
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        k, result = len(user_word), user_word
        for valid_word in valid_words:
            diff_num = diff_function(user_word, valid_word, limit)
            if  diff_num < k and diff_num <= limit:
                k, result = diff_num, valid_word
        return result
    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    def compare_letter(ith = 0):
        if ith >= min((len(goal),len(start))):
            return abs(len(goal)-len(start))
        if start[ith] != goal[ith]:
            return 1 + compare_letter(ith + 1)
        else:
            return compare_letter(ith + 1)
    return compare_letter()
    # END PROBLEM 6


def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'

    # here's a question, if I use user-defined functions below to represent 
    # the return expression in operate_with_i(), it will be wrong
    # def add_diff(i):
    #     return 1 + operate_with_i(start[:i]+goal[i]+start[i:],i+1)
    # def remove_diff(i):
    #     return 1 + operate_with_i(start[:i]+start[i+1:],i+1)
    # def subsitute_diff(i):
    #     return 1 + operate_with_i(start[:i]+goal[i]+start[i+1:],i+1)

    def operate_with_i(start, i = 0):
        if i >= len(start):
            return len(goal) - len(start)
        elif i >= len(goal):
            return len(start) - len(goal)
        elif start[i] == goal[i]: # Fill in the condition
            # BEGIN
            return operate_with_i(start, i + 1)
            "*** YOUR CODE HERE ***"
            # END
        elif start[i+1:i+2] == goal[i+1:i+2]:
            return 1 + operate_with_i(start[:i]+goal[i]+start[i+1:],i+1)
        elif (start[i] == goal[i+1:i+2] and len(start) < len(goal)) or start[i:i+2] in goal[i+1:i+4]:
            # Feel free to remove or add additional cases
            # BEGIN
            "*** YOUR CODE HERE ***"
            return 1 + operate_with_i(start[:i]+goal[i]+start[i:],i+1)
            # END
        elif (start[i+1:i+2] == goal[i] and len(start) > len(goal)) or goal[i:i+2] in start[i+1:i+4]:
            return 1 + operate_with_i(start[:i]+start[i+1:],i+1)
        else:
            return 1 + operate_with_i(start[:i]+goal[i]+start[i+1:],i+1)
    return operate_with_i(start)

    # if :
    #     pass

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def compare_letter(ith = 0):
        if ith >=len(prompt):
            return 1
        elif ith >= len(typed):
            return ith/len(prompt)
        elif typed[ith] == prompt[ith]:
            return compare_letter(ith + 1)
        else:
            return ith / len(prompt)
    result = compare_letter()
    d = {'id':id,'progress':result}
    send(d)
    return result
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    result = [[] for _ in range(n_players)]
    for i in range(n_words):
        player, min_time, fword = [], 1000, ""
        for j in range(n_players):
            time = elapsed_time(word_times[j][i+1])-elapsed_time(word_times[j][i])
            # print("player",j,i,"th","word:",word(word_times[j][i+1]),"time",time,"margin",margin)
            if min_time > time + margin: #over, remove
                player, min_time, fword = [j], time, word(word_times[j][i+1])
                # print(1,min_time,time+margin,player)
            elif min_time >= time and time + margin >= min_time: # within margin, change and add
                player, min_time, fword = player+[j], time, word(word_times[j][i+1])
                # print(2,min_time,time+margin,j)
            elif min_time <= time and min_time + margin >= time:
                player = player+[j]
        #         print(3,min_time,time+margin,player)
        #     else:
        #         print(4,player)
        # print(player)
        for j in player:
            result[j].append(fword)
    return result

                        

    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)