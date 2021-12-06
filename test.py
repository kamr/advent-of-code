# def kamran(x, y):
#     return x + y
#
# print(kamran(5, 10))
#
# c = [4+5, 2, 3, "dog"]
# c.append("hello")
# print(c)
# print(c[0])
#
# xs = [4, 6, 7]
# xss = [xs]
#
# print(xs)
#
# # for x in xs:
# #     print(x)
#
# for i in range(len(xs)):
#     print(i)

x = "asdsda"

# if x == "hello":
#     print("test")
# else:
#     print("aaa")

match x:
    case "hello":
        print("test")
    case "bye":
        print("b")
    case _:
        print("c")
