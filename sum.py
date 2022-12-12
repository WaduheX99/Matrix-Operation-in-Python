input1 = [[2,5,4],
         [5,4,7],
         [5,6,9]]

input2 = [[6,5,4],
         [5,4,7],
         [5,3,9]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

## Loop baris
for i in range (0, len(input1)) :
    ## Loop Kolom
    for j in range (0, len(input2)) :
        result[i][j] = input1[i][j] + input2[i][j]

for r in result :
    print(r)