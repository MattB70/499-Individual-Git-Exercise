# Sorting Integers or Strings.
# Matthew Borle
# September 14, 2021

# Python 2.7.15


while True:
    input_type = raw_input("Integers or Strings? (Ii/Ss): ")

    if input_type == "I" or input_type == "i":
        print "Integers selected"
        array = raw_input("Input integers seperated by spaces:\n")
        print "Input:\t" + array
        array = array.split(" ")
        array = [x for x in array if x.isdigit()] # remove any non numeric values
        array.sort(key=int)
        print "Output:\t" + " ".join(array)
        break;
    
    if input_type == "S" or input_type == "s":
        print "Strings selected"
        array = raw_input("Input strings seperated by spaces:\n")
        print "Input:\t" + array
        array = array.split(" ")
        array = [x for x in array if not x.isdigit()] # remove any non string values
        array.sort(key=str)
        print "Output:\t" + " ".join(array)
        break;

    if input_type == "T" or input_type == "t": # Test
        print "Tests selected"
        print "String Input:\torange apple grape strawberry blackberry"
        strings = "orange apple grape strawberry blackberry"
        strings = strings.split(" ")
        strings = [x for x in strings if not x.isdigit()] # remove any non string values
        strings.sort(key=str)
        print "String Output:\t" + " ".join(strings)
        print "Integer Input:\t2 9 5 0 1 10 4 21 9 1"
        integers = "2 9 5 0 1 10 4 21 9 1"
        integers = integers.split(" ")
        integers = [x for x in integers if x.isdigit()] # remove any non numeric values
        integers.sort(key=int)
        print "Integer Output:\t" + " ".join(integers)
        break;

    else: # User input invalid argument.
        print "Invalid input type. Try again.\n"

