sentence = input("Enter a sentence here:\n")
sen_nums = len(sentence.replace(" ", "").replace(".", "").replace("-", ""))

vowels = "a e i o u A E I O U".split()
consonants = "b c d f g h j k l m n p q r s t v w x y z B C D F G H J K L M N P Q R S T V W X Y Z".split()

vowel_nums = 0
conso_nums = 0

for char in sentence:
    if char in vowels:
        vowel_nums += 1
    elif char in consonants:
        conso_nums += 1

print(f"Your sentence has {sen_nums} letters with {vowel_nums} vowels, and {conso_nums} consonants.")
input("\nPress enter to exit the program...\n")