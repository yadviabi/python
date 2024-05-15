
input = [2, 4, 6, 8, 6, 8, 1 ,2]
output = []
dict = {}
for elem in  input:
        if not elem in dict.keys():
            output.append(elem)            
            dict[elem] = True


print (output)

    

