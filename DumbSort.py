# Sorting Integers or Strings.
# Matthew Borle
# September 14, 2021

# Python 2.7.15


while True:
    input_type = raw_input("Integers or Strings? (Ii/Ss): ")

    if input_type == "I" or input_type == "i":
        print "Integers selected"
        array = raw_input("Input integers seperated by spaces:\n")
        print array

        break;
    
    if input_type == "S" or input_type == "s":
        print "Strings selected"
        array = raw_input("Input strings seperated by spaces:\n")
        print array

        break;

    else:
        print "Invalid input type. Try again.\n"
