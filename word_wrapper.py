from layout_settings import calculate_task_characters_per_line

class WordWrapper:
    def __init__(self, text, characters_per_line):
        self.characters_per_line = characters_per_line
        self.lines = []
        self.current_line = ""
        self.words = text.split(" ")


    def wrap_words(self):
        for word in self.words:
            if (self.word_fits_on_current_line(word)):
                self.add_to_current_line(word)
            else:
                self.save_current_line()
                self.start_new_line(word)
        self.save_current_line()
        return self.lines

    def word_fits_on_current_line(self, word):
        current_line_length = len(self.current_line)
        requires_a_space = current_line_length > 0
        line_length_with_word = current_line_length + len(word)
        if requires_a_space:
            line_length_with_word += 1
        return line_length_with_word <= self.characters_per_line

    def add_to_current_line(self, word):
        first_word = len(self.current_line) == 0
        if first_word:
            self.current_line = word
        else:
            self.current_line += f" {word}"

    def save_current_line(self):
        # If the first word does not fit on a line we will try to save our empty initial line, check for this
        if len(self.current_line) > 0:
            self.lines.append(self.current_line)

    def start_new_line(self, word):
        # If the word is longer than a line we need to wrap mid word
        characters = list(word)
        while len(characters) > self.characters_per_line:
            string_before_cutoff = "".join(characters[0:self.characters_per_line])
            self.lines.append(f"{string_before_cutoff}")
            characters = characters[self.characters_per_line:]
        self.current_line = "".join(characters)
