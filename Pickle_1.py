import pickle
fruits =['apples','oranges','bananas']
x = 7
y= 3.14
nuts =['pecans','almond']
grades = [99,100,85,77,56]

with open('myData.pkl','wb') as f:
    pickle.dump(fruits,f)
    pickle.dump(x,f)
    pickle.dump(nuts,f)
    pickle.dump(grades,f)
    pickle.dump(y,f)
    
with open('myData.pkl','rb') as whatever:
    a = pickle.load(whatever)
    b = pickle.load(whatever)
    c= pickle.load(whatever)
    d= pickle.load(whatever)
    e = pickle.load(whatever)
print(a)
print(b)
print(c)
print(d)
print(e)




