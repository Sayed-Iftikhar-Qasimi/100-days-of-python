class Question:
    def __init__(self,text, answer):
        self.text = text
        self.answer = answer

    def display(self):
        print(f"Text: {self.text}, Answer: {self.answer}")

