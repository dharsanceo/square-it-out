start = int(input("Start: "))
end = int(input("End: "))
squares = [n*n for n in range(start, end+1)]
even = [s for s in squares if s % 2 == 0]
odd = [s for s in squares if s % 2 != 0]
print("Squares:", squares)
print("Even:", even)
print("Odd:", odd)
