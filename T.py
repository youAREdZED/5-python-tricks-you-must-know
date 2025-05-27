#1
list1 = ["a", "b", "c"]
list2 = [i for i in list1 if i == "a"]

print(list2)



#2
even_nums = [i for i in range(10) if i % 2 == 0]

print(*even_nums, sep="\n")



#3
list1 = ["pride", "toyota", "benz", "bmw"]
list2 = ["a", "b", "c"]

print(list1 if len(list1)>len(list(2)) else list2)



#4
wellcome = "Hello %s"

print(wellcome % "CodeForLife")



#5

pos = [f"({x}, {y})" for x in range(1,10+1) for y in range(1,10+1)]

print(*pos, sep="\n")