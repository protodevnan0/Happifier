import random;


print ("");
print ("");
print (" Welcome to Happifier. It will generate random inspirational quotes for You!");
print ("");
print ("");



first = ["Be ", "Don't ", "Do ", "Smile ", "Move on, ", "Forget ", "Look "];

second = ["at ", "for ", "forward ", "keep ", "cuddle ", "whistle ", "awkwardly ", "what ", "let ", "break ", "fight ", "fly ", "buy ", "cry ", "breathe ", "urinate ", "vomit ", "stop ", "touch ", "watch ", "smell "];

third = ["more ", "cookies ", "farts ", "cars ", "nuggets ", "poop ", "love ", "dogs ", "aliens ", "cats ", "pennies ", "chocolate ", "money ", "music ", "depression ", "orgasm ", "ice cream ", "juice ", "feet ", "apples ", "movies "]


quote_gen = random.choice(first) + random.choice(second) + random.choice(third);

print (" " + quote_gen);

