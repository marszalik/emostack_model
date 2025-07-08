class EmoThoughtTrigger:

    def __init__(self):

        # subject to be considered by the AI for emotion creation
        self.subject = ""

        # context in which subject is considered
        self.context = ""

        # source of the thought and context
        self.source = ""

    def combined(self):
        combined = self.subject + " \n\non context: " + self.context
        return combined
