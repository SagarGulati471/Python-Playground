# a = [1,2,3,4,5]
# b = [1,2,3,4,5]
# c = [0,0,1]
# d = [1,1,1,1, 0.001]
# print(any(c))
# print(all(d))

# print(dict.fromkeys(a,[]))


# a = {1,2,3,4,5,6,91}
# b = {6,7,8,9}
# c = {99,344 }
# # print(type(a))
# print(a | b | c)
# a |= b | c
# # print(f'a |= b | c = {a | b | c}')

# print(f'a = {a}')


class test:
    def __init__(self):
        print('init called')

    # def __repr__(self):
    #     return "test instance __repr__"

    def __str__(self):
        print(super().__str__())
        return "test instance __str__"

t = test()
# print(t.__repr__())
print(t.__str__())
# print(t)