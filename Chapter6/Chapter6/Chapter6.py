#Fun With Arrays

animal_array = ["Giraffe", "Emu", "Ostrich", "Chimpanzee", "Elephant"]
#print(animal_array)
#for i in animal_array:
#    print(i)

animal_array.append("Hyena")
animal_array.append("Kangaroo")
print(animal_array)

animal_array.remove("Emu")
#print(animal_array)
#print("Number of elements: ", len(animal_array))
#print("Last index: ", len(animal_array) - 1)

for i in range(len(animal_array) + 1):
    print(animal_array[i])