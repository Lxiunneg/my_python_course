class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    # Your code here
    def is_worth_it(self):
        return False if self.draft - (1.5 * self.crew) <= 20 else True