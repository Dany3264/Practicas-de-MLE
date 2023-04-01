#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
#inclusive.

numbers = list(range(1, 21))
print(numbers)

#4-4. 4-4. One Million: Make a list of the numbers from one to one million, and then
#use a for loop to print the numbers.

#4.5 Summing a Million: Make a list of the numbers from one to one million,
#and then use min() and max() to make sure your list actually starts at one and
#ends at one million. Also, use the sum() function to see how quickly Python can
#add a million numbers.

#big_list = list(range(1, 1_000_000))

#for number in big_list:
#	print(number)
#min(big_list)
#max(big_list)

#sum(big_list)
#print(sum(big_list))

#4.6 Odd Numbers: Use the third argument of the range() function to make a
#list of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
	print(number)

#4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
#print the numbers in your list.

multiples_of_3 = list(range(3, 31, 3))
for multiples in multiples_of_3:
	print(multiples) 

#4-8. Cubes: A number raised to the third power is called a cube. For example,
#the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
#is, the cube of each integer from 1 through 10), and use a for loop to print out
#the value of each cube.

cubes = []
for val in range (1, 11):
	cube = val ** 3
	cubes.append(cube)

print(cubes)

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the
#first 10 cubes.

new_cubes = [value**3 for value in range(1, 11)]