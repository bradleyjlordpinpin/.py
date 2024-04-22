def remove_matching_balls(balls, index, color):
    balls.insert(index, color)
    while balls: # continue looping while the list is not empty
        i = index - 1
        j = index + 1
        while i >= 0 and balls[i] == color:
            i -= 1
        while j < len(balls) and balls[j] == color:
            j += 1
        if j - i - 1 >= 3: # if there are 3 or more matching colors
            del balls[i+1:j] # delete the matching colors
            index = i # set the new index to the leftmost matching color
            
            # set the new color to the color immediately to the left
            # of the leftmost matching color, if there is one
            if i >= 0:
                color = balls[i] 
            # otherwise, set the new color to the color immediately to
            # the right of the rightmost matching color
            else:
                color = balls[j]
        else:
            break # no more matching colors, exit the loop

balls = ['r', 'r', 'y', 'y', 'r', 'b', 'r', 'r', 'b']

while balls:
    print(balls)
    color = input("Color: ")
    index = int(input("Index: "))
    remove_matching_balls(balls, index, color)
    
print("You Win")


