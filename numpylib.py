import numpy as np

a = np.array([1,2,3])
# print(a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
# print(b)
#
# ## Get Dimension
# print(a.ndim) #print the dimension of the array
# print(b.ndim) #2 Dimension of b array
#
#
# ##Get Shape
# print(b.shape) #(2,3) shape of the array


##Get Type
# print(a.dtype) # Gives the data type

##Can specify the size while defining a = np.array([1,2,3]),dtype = 'int32')


##Get Size
# print(a.itemsize) #Print the size of the item
# print(a.size) #Prints number of values in the array
# print(a.size * a.itemsize) #Prints total size of the array
# print(a.nbytes)  #Prints total size of the array

##Float size are bigger than integer


## Accessing /Changing specific elements, rows, columns, etc

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a)

##Get a speccific element [r,c]
# print(a[1,5])  #Prints 13 from the above array

## Get a specific row
# print(a[0,:]) #Gives first row

##Get a specific column
# print(a[:,2]) #gives third column

# #change the element
# a[1,5] = 20
# print(a)
#
#
# ##Change the entire column
# a[:,2] = 5 #Changing the entire row to 5
# print(a)
# a[:,2] = [1,2] #Changing the rows with different values
# print(a)
#
# ##3-D Example
# b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(b)
#
# ## Get specific element
# print(b[0,1,1])
#
#
# ##Replace
# b[:,1,:] = [[9,9],[8,8]]
# print(b)


# print(np.zeros((2,3))) #Gives a 2X3 matrix with all zeros
# print(np.ones((4,2))) #Gives a 4X2 matrix with all ones
#
#
# print(np.full((2,2),99)) #Gives a 2X2 matrix with all 99's



##Random decimal numbers
# print(np.random.rand(4,2)) #Generates 4X2 matrix with random decimal numbers

##Random Integer values
# print(np.random.randint(-4,7,size=(3,3))) #Generates a random 3X3 array with numbers between -4 and 7


## Identity matrixx
# print(np.identity(5))


## Copying Arrays
#
# a = np.array([1,2,3])
# b = a
# b[0] = 100 ## Both a and b getts changes
#
# b= a.copy()
# b[0] = 524 ##Only b changes



# #Mathematics
# a = np.array([1,2,3,4])
# print(a**2)
# b = np.array([5,6,7,8])
# print(a+b)


##Take a sin
# print(np.sin(a))


# ##Linear Algebra
# a = np.ones((2,3))
# b = np.full((3,2),2)
# print(np.matmul(a,b))
#
#
#
# ## Find the determinant
# c = np.identity(3)
# print(np.linalg.det(c))



# ## Statistics
# stats = np.array([[1,2,3],[4,5,6]])
# print(np.min(stats))
# print(np.max(stats))




##Reorganizing/Rearranging of arrays
# before = np.array([[1,2,3,4],[5,6,7,8]])
# print(before)
# after = before.reshape((4,2))
# print(after)


##Vertical stacking
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2,v1,v2]))


















