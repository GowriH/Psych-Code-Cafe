from Classes import Response, Person, Questions

##
# @author Aryan Wadhwani, Gowri Harish, Keerthana Vegesna, Preksha Ravikumar
##
exit = False
number = int(input("Number of Players: "))
file_used = open("UsedQuestions.txt", 'w')
file_used.close()
players = []
for i in range(number):
    players.append(Person(input("Enter your username: ")))
while not exit:
    try:
        a_question = Questions()
        print(a_question.question)
        responses = []
        for player in players:
            response = Response(input("Please {}🥺🥺🥺, enter an answer: ".format(player.name)), player)
            responses.append(response)
        for i in range(len(set(responses))):
            responses[i].index = i
            print(i + 1, ": ", responses[i].response_string)
        for player in players:
            wrong = False
            counter = 0
            while not wrong:
                my_vote = int(input("Please {}🥺🥺🥺, Select your vote".format(player.name)))

                for response in responses:
                    if my_vote - 1 == response.index:
                        if player != response.person:
                            response.add_vote()
                            wrong = True
                        else:
                            counter += 1
                            if counter <= 0:
                                print("Please select someone else")
                            if counter == 6:
                                print("You will be missed")
                                players.remove(player)
                                wrong = True
        for response in responses:
            response.add_score()
        # PRINTING OUT RESPONSES
        print("_______SCORES________")
        for player in players:
            print(player.name, ": ", player.score)
        print()
    except:
        file_used = open("UsedQuestions.txt", 'w')
        file_used.close()
        exit = True