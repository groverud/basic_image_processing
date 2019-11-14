import utilities

def rotate_90_degrees(image_array, direction = 1):
	'''
	(list, int) -> (list) 
	Takes in image array and direction of rotation and returns a rotated image array

	rotate_90_degrees([[1,0,0],[0,1,0],[0,0,1]], direction = 1)
	>> [[0,0,1],[0,1,0][1,0,0]]
	'''
    m = len(image_array[:][1])                                                       
    n = len(image_array[1][:]) 
        
    print(m,n)

    im = image_array.copy()
    new = []
    nl = []

    for y in range(n):
        nl.append(0)
    for u in range(m):     
        new.append(nl.copy())

    for i in range(n//2):
    
        temp1 = im[i][i:n-i]
        temp2 = [row[n-i-1] for row in im[i:m-i]]
        temp3 = (im[m-1-i][i:n-i])
        temp3.reverse()
        temp4 = [row[i] for row in im[i:m-i]]
        temp4.reverse()                                                

 
        if(direction == 1):
            ctr = 0
            for c1 in range(i,n-i):
                  
                new[i][c1] = temp4[ctr]
                print(temp4[ctr])                                     # 1
                new[m-1-i][n-c1-1] = temp2[ctr] 
                print(temp2[ctr])                                # 3
                ctr = ctr + 1

            ctr = 0
            for r1 in range(i, m-i):
                
                new[r1][n-1-i] = temp1[ctr] 
                print(temp1[ctr])                                # 2
                new[m-r1-1][i] = temp3[ctr]
                print(temp3[ctr])                                     # 4
                ctr = ctr +1
	

        elif(direction == -1):
            ctr = 0
            for c1 in range(i,n-i):
                  
                new[i][c1] = temp2[ctr]
                print(temp4[ctr])                                     # 1
                new[m-1-i][n-c1-1] = temp4[ctr] 
                print(temp2[ctr])                                # 3
                ctr = ctr + 1

            ctr = 0
            for r1 in range(i, m-i):
                
                new[r1][n-1-i] = temp3[ctr] 
                print(temp1[ctr])                                # 2
                new[m-r1-1][i] = temp1[ctr]
                print(temp3[ctr])                                     # 4
                ctr = ctr +1
                       

    new[m//2][n//2] = im[m//2][n//2]            
    return new

def flip_image(image_array, axis = 0):
	'''
	(list, int) -> (list)
	Takes in an image array/list and axis of flipping, and returns the flipped image.

	flip_image([[1,0,0],[0,1,0],[0,0,1]], axis = 0)
	>> [0,0,1],[0,1,0],[1,0,0]
	''' 
    m = len(image_array[:][1])                                                        # len rows
    n = len(image_array[1][:])     
    print(image_array)
    

    imli = image_array.copy()

    if(axis == 0):                                                          #column flipper
        for r in range(m):
            for c in range(n//2):
                    
                temp = imli[r][c]
                print(temp)
                imli[r][c] = imli[r][n-c-1]
                imli[r][n-c-1] = temp
                print(imli[r][c])
                    
        return imli
                

    elif(axis == 1):                                                         #row flipper
        for c in range(n):
            for r in range(m//2):

                temp = imli[r][c]
                imli[r][c] = imli[m-r-1][c]
                imli[m-r-1][c] = temp

        return imli
                

    elif(axis == -1):                                                        #diagonal(x=y) flipper
        for r in range(m):
            for c in range(n-r-1):

                temp = imli[r][c]
                imli[r][c] = imli[m-c-1][n-r-1]
                imli[m-c-1][n-r-1] = temp

        return imli

def invert_grayscale(image_array):
	'''
	(list) -> (list)
	Takes in a grayscacle image array and returns the inverted image array.
	
	'''

	m = len(image_array[:][1])                                                        # len rows
    n = len(image_array[1][:])
    
    im = image_array.copy()

    for r in range(m):
        for c in range(n):
            im[r][c] = 255 - im[r][c] 

    return im

def crop(image_array, direction, n_pixels):
	'''
	(list, string, int) -> (list)
	Takes in a the image array, the direction to crop in and the number of pixels to crop in the given direction, and returns thr cropped image array.

	crop([[1,2,3],[4,5,6],[7,8,9]], 'up', 1)
	>> [[1,2,3],[4,5,6]]
	'''
    m = len(image_array)                                                        # len rows
    n = len(image_array[1][:])

    im = image_array.copy()

    if (direction == "left"):
        neew = [row[0:n-n_pixels] for row in im[:]]
        return neew

    elif (direction == "right"):
        neew = [row[n_pixels:n] for row in im[:]]
        return neew     

    elif (direction == "up"):
        return im[0:n-n_pixels][:]

    elif (direction == "down"):
        return im[n_pixels-1:m][:]

def rgb_to_grayscale(rgb_image_array):

    '''
	(list) -> (list)
	Takes in an rgb image array, and returns the converted grayscale image array.

	[
    [ [255, 10, 0],[0,15, 42],[4, 200, 190] ],
    [ [200, 20, 5],[4, 200, 190],[22, 59, 240] ],
    [ [143, 0, 1],[78, 31, 199],[159, 180, 217] ]
    ]
    '''
    
    m = len(rgb_image_array)                                                        # len rows
    n = len(rgb_image_array[1][:])
    print(m,n)

    rgim = rgb_image_array.copy()
    print(rgim)

    nl=[]
    new=[]

    final = []

    for y in range(n):                                      # making 0 array
        nl.append(0)    
    for u in range(m):     
        new.append(nl)


    for r in range(0,m):                                  
        row=[]                                   
        for c in range(0,n):
            row.append(((0.2989*rgim[r][c][0]) + (0.5870*rgim[r][c][1]) + (0.1140*rgim[r][c][2])))
        final.append(row)
    
    return final

def invert_rgb(image_array):
	'''
	(list) -> (list)
	Takes in an rgb image array, and returns the inverted image array.

	'''

    m = len(image_array)                                                        # len rows
    n = len(image_array[1][:])


    rgim = image_array.copy()

    for r in range(m):
        for c in range(n):
            for i in range(3):
                rgim[r][c][i] = 255 - rgim[r][c][i] 

    return rgim
    


if (__name__ == "__main__"):
    file = 'robot.png'
    utilities.write_image(rgb_to_grayscale(
        utilities.image_to_list(file)), 'gray.png')
