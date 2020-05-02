notes = []

print ("... NOTES AVERAGE ...")

name = input("Enter student name and surname... ")

MathNote = float(input("Enter note of Math for {} ... ".format(name)))
notes.append(float(MathNote))

LiteratureNote = float(input("Enter note of Literature for {} ... ".format(name)))
notes.append(float(LiteratureNote))

PhysicalNote = float(input("Enter note of Physical for {} ... ".format(name)))
notes.append(float(PhysicalNote))

average = sum(notes)/len(notes)

if(average > 6):
    message = "Approved."
    if(average > 9):
        message = message + " Additional, The student is prominent."
elif (average < 4 ):
    message = "Insufficient."
else:
    message = "To recuperative."

print("\nThe average note of {} is {} and is ... {}".format(name,str(average),message))






