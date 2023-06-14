def e_only(phrase):
    words = list(phrase.split(" "))
    just_e = [word for word in words if word.startswith("E")]
    return just_e


phrase = input("I'M HUNGRY! FEED ME SOME WORDS! ").upper()
print("THANKS! I'LL GIVE YOU BACK THE 'E' WORDS'!")
print(e_only(phrase))

# words = phrase.split(" ")
# for word in words:
#     if word.startswith("E"):
#         print(word)
