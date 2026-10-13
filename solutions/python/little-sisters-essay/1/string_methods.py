"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed."""

    return title.title()
#print(capitalize_title("my hobbies"))



def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present."""

    return sentence.endswith(".")
#print(check_sentence_ending("I like to hike, bake, and read."))



def clean_up_spacing(sentence):
    """Trim any leading or trailing whitespace from the sentence."""

    return sentence.strip()
#print(clean_up_spacing(" I like to go on hikes with my dog.  "))



def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one."""
    
    return sentence.replace(old_word, new_word)
#print(replace_word_choice("I bake good cakes.", "good", "amazing"))