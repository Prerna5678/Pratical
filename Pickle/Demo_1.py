#pip install pickle
import pickle

lst = [1, 2, 3, 4, 5, "hi"]

f = open("P_demo.txt", "wb")
pickle.dump(lst, f)
# print(help(pickle.dump))
