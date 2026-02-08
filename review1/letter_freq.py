#index: a number that selects individual part of a list or string (letter)
#Git notes:
#git pull: updates local (e.g desktop) code
#git status: Shows branch, changes made
#git push: updates remote (repository) code
#git add: command that adds code to repository; part of gitpush
#git commit: what stores code, message to indicate changes
def letter_freq():
    letter = input("Enter letter to test it's frequency in a word(s): ")
    string = input("Enter word(s):")
    lfd = {}
    lfd[letter] = 0
    for ltr in range(len(string)):
        string[ltr]
        if string[ltr] == letter:
            lfd[string[ltr]] += 1
    return(lfd[letter])
print("Letter frequency: " + str(letter_freq()))