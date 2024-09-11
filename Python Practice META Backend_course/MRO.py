# # # # # class A:
# # # # #     pass
# # # # # class B(A):
# # # # #     pass
# # # # # class C(B):
# # # # #     pass
# # # # # print(help(C))

# # # # # Example 1
# # # # # class A:
# # # # #    def a(self):
# # # # #        return "Function inside A"

# # # # # class B:
# # # # #     def a(self):
# # # # #         return "Function inside B"

# # # # # class C(B,A):
# # # # #     pass

# # # # # # Driver code
# # # # # c = C()
# # # # # print(c.a())

# # # # # class A:
# # # # #     def b(self):
# # # # #         return "Function inside A"

# # # # # class B:
# # # # #     def b(self):
# # # # #         return "Function inside B"

# # # # # class C(A, B):
# # # # #     # def b(self):
# # # # #         # return "Function inside C"
# # # # #     pass

# # # # # class D(C):
# # # # #     pass

# # # # # d = D()
# # # # # print(d.b())

# # # # class A:
# # # #     def c(self):
# # # #         return "Function inside A"

# # # # class B:
# # # #     def c(self):
# # # #         return "Function inside B"

# # # # class C(A, B):
# # # #     def c(self):
# # # #         return "Function inside C"

# # # # class D(A, C):
# # # #     pass

# # # # d = D()
# # # # print(d.a)

# # # class A:
# # #     def b(self):
# # #         return "Function inside A"

# # # class B:
# # #     pass

# # # class C:
# # #     def b(self):
# # #         return "Function inside C"

# # # class D(B, C, A):
# # #     pass

# # # class D(C):
# # #     pass

# # # d = D()
# # # print(d.b())
# # a = 5
# # class A:
# #       a = 7
# #       pass

# # class B(A):
# #       pass

# # class C(B):
# #       pass

# # c = C()
# # print(c.a())
# value = 7
# class A:
#     value = 5

# a = A()
# a.value = 3
# print(value)
bravo = 3
b = B()
class B:
    bravo = 5
    print("Inside class B")
c = B()
print(b.bravo)