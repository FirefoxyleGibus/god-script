# Get a value and shows it with different cast

store(value,toInt(input("Enter a number >>> ")));
show("String : ",toString(value),"\n"); # String
show("Int : ",value,"\n"); # Int
show("Char : ",toChar(value),"\n"); # Character {value}th
show("Uni : ",toUni(toString(value)),"\n"); # Unicode value of the character {value}
