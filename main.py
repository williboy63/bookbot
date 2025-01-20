
def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return print(file_contents)

def word_count():

    count = 0

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        words = file_contents.split()

        for w in words:
            count +=1

    return count

def letter_count():
    
    final_dict = {}

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower_contents = file_contents.lower()

        for char in lower_contents:
            if char in final_dict:
                final_dict[char] += 1
            else:
                final_dict[char] = 1


        return print(final_dict)
        
def report():
     
     report_dict = {}
    
     with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower_contents = file_contents.lower()

        for l in lower_contents:
            if l.isalpha() == True:
                if l in report_dict:
                    report_dict[l] += 1
                else:
                    report_dict[l] = 1

        return report_dict
     
print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count()} words were found in the document")
print("")
list = []

for x in report():
    list.append(x)

for x in range(0, len(list)):
    print(f"The '{list[x]}' character was found {report()[list[x]]} times")

print("--- End report ---")


    



