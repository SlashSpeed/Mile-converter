while True:
    mile_base = 1.609
    question = int(raw_input("Please enter your desire kilometers to convert to miles, here: "))
    answer = question * mile_base
    print ("That's " + str(answer) + " in miles.")

    question_2 = raw_input("If you wish to continue converting, please type in yes, otherwise type in no.")

    if question_2 == "no":
        print ("Thank you for using my converter. Goodbye.")
        break
