##for a list of words, print each word on a separate line, in uppercase
##turn that into a function that only prints words beginning with "e"

input_string = input("I'M HUNGRY! FEED ME SOME WORDS! ")
words = input_string.split(" ")
big_words = [x.upper() for x in words]


def e_only(big_words):
    for x in big_words:
        if x.startswith("E"):
            print(x)
        else:
            print("I ONLY LIKE WORDS THAT BEGIN WITH 'E'")
