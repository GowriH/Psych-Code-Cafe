from random import choice


class Response:
    def __init__(self, response_string, person):
        self.response_string = response_string
        self.person = person
        self.vote = 0
        self.index = -1

    def add_vote(self):
        self.vote = self.vote + 1

    def add_score(self):
        self.person.score += self.vote

    def __repr__(self):
        return "{self.person, self.response_string, self.vote}"

    # def display(self):
    #     print(self.vote, self.person.name)


class Questions:
    def __init__(self):
        self.question = self.read_questions()

    def read_questions(self):
        file = open("NewQuestions.txt", 'r')
        file_used = open("UsedQuestions.txt", 'r')
        questions = file.readlines()
        used_questions = file_used.readlines()

        question = choice(questions)

        if question in used_questions:
            file_used.close()
            file.close()
            return self.read_questions()
        else:
            file_used.close()
            file_used = open("UsedQuestions.txt", 'a')
            file_used.write(question)
            file_used.close()
            file.close()
            return question
    #
    # def __repr__(self):
    #     return f"{self.question}"
    #
    # def display(self):
    #     print(self.question)


class Person:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.winner = False

    def __repr__(self):
        return "{self.name}"
