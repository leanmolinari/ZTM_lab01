# exercise

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

#for laps in range(2):
#    for row in picture:
#        for pixel in row:
#            if (pixel == 1):
#                print('*', end= '')
#            else:
#               print(' ', end = '')
#        print('')



# for repease in an easy way, I'm going to put the above code in a funciton
def show_tree():
    for row in picture:
        for pixel in row:
            if (pixel == 1):
                print('*', end= '')
            else:
                print(' ', end = '')
        print('')

show_tree()
show_tree()
show_tree()
