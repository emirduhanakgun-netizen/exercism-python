"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    
    return "un" + word
#print(add_prefix_un("happy"))


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words."""
    
    seperate = " :: " + vocab_words[0]
    return seperate.join(vocab_words)
#print(make_word_groups(['en', 'close', 'joy', 'lighten']))


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind."""
    
    lastword = word[:-4]
    if lastword[-1] == "i":
        lastword = lastword[:-1] + "y"
    return lastword    
#print(remove_suffix_ness("heaviness"))


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""

    new_word = sentence.split()[index]
    clean_word = new_word.strip(".,;:")
    return clean_word + "en"
#print(adjective_to_verb("I need to make that bright.", -1))