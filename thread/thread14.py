from threading import Thread


def method(name, sal):
    print(name, sal)


t1 = Thread(target=method, args=("raj", 90000))
t2 = Thread(target=method, kwargs={"name": "kuj", "sal": 900})
# help(t1)
t1.start()
t2.start()
# print(t1.name)
# print(t1.getName)

# a =("welcome")
# print(type(("welcome")))
# print(type(("welcome",)))
# a = "welcome"
# for i in a:
#     print(i)
