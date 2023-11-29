class MyString:
    def __init__(self, value=""):
        self.value = value

    def is_sentence(self):
        if isinstance(self.value, str):
            return self.value.endswith('.')
        return False

    def is_question(self):
        if isinstance(self.value, str):
            return self.value.endswith('?')
        return False

    def is_exclamation(self):
        if isinstance(self.value, str):
            return self.value.endswith('!')
        return False

    def count_sentences(self):
        if isinstance(self.value, str):
            # Updated logic to count sentences
            sentences = [sentence.strip() for sentence in self.value.split('.') if sentence.strip()]
            return len(sentences)
        return 0
