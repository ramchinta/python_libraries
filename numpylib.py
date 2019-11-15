import numpy as np

a = np.array([100,200,300])
print(type(a))
'''
mypythonlist = [[[1,9,8],[7,3,7]],[[2.3,6,8],[5,0,6]]]
c = np.zeros((2,3,4))
print(c)
d = ([[1,2,3],[4,5,6]])
e = c.flatten()
print(d.shape)
print(e.shape)
print(e)

f= np.array([1,2,3])
g= np.array([4,5,6])
print("Horizontal Apped:",np.hstack((f,g)))
print('Vertical Append :',np.vstack((f,g)))


a =np.arange(1,11)
print(a)
a = np.arange(1,14,4)
print(a)

a=np.matrix(np.ones((4,4)))
b=np.asarray(a)
print(b)

#linspace()
#numpy.linspace(start,stop,num,endpoint)
print(np.linspace(1,600,10,False))
print(np.logspace(1,600,10,False))

a = np.array([[1,2,3],[4,5,6]])
a[:,0]=50
print(a)

#Broadcasting

a=np.arange(1,11)
print(a)
a[0:3]=50
print(a)
'''

#scalar operations
app = np.arange(1,11)
print(np.sqrt(app))
print(app)









