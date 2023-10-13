"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val[0])
            val.pop(0)

        return text


# Here's a story to get you started

story = Story(
    ["name", "noun", "noun", "feeling", "verb", "verb", "verb", "noun", "noun", "place",
    "feeling", "adjective", "noun" ],
    '''This weekend I am going camping with {name}. I packed my {noun}, sleeping bag,
    and a {noun}. I am so {feeling} to {verb} in a tent. We are going to hike, fish and {verb}.
    We might even {verb} a {noun}. If I see a {noun}, I will bring it to {place} as a pet for
    show and tell. At night we will tell {adjective} {adjective} stories around the
    campfire and roast {noun}.'''
)