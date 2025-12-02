from threading import Thread


def method(a):
    print(a)


t1 = Thread(target=method, args=("welcome",))
# help(t1)
t1.start()
# print(t1.name)
# print(t1.getName)

# a =("welcome")
# print(type(("welcome")))
# print(type(("welcome",)))
# a = "welcome"
# for i in a:
#     print(i)
