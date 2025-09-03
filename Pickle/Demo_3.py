import pickle

lst = [1, 2, 3, 4, "hii"]
a = pickle.dumps(lst)
print(a)

b = pickle.loads(a)
print(b)
