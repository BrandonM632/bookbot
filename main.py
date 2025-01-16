def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        lowercase = file_contents.lower()
        count = len(words)
        letter_count = {}
        for i in range (len(lowercase)):
            if (lowercase[i] < "a" or lowercase[i] > "z"):
                # ignore any character that isn't a letter
                pass
            elif (lowercase[i] in letter_count) == False:
                # if a character is not in the dictionary yet add it
                letter_count[lowercase[i]] = 1
            #increment the count of characters in the dictionary 
            else: letter_count[lowercase[i]] +=1

        #sort letter_count dictionary from highest to lowest
        letter_tuple = sorted(letter_count.items(), key=lambda x:x[1], reverse = True)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count} words found in the document\n")
        for pair in letter_tuple:
            print(f"The {pair[0]} character was found {pair[1]} times")
        print("--- End report ---")
main()