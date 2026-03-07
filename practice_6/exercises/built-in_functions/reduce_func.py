from functools import reduce

informaion = ["Python", "is", "good"]
res = reduce(lambda x, y: x + " " + y, informaion)

print(res)