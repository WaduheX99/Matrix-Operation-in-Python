matrixKosong = []
i1 = [0] * (9)

## Membuat matrix kosong 3x3
for x1 in range(3) :
    matrixKosong.append([])
    for y1 in range(3) :
        matrixKosong[x1].append(0)

## Menginputkan elemen" matrix
m = 0
for x in range(0, 8 + 1, 1):
    print("masukkan elemen ke - " + str(x + 1))
    i1[m] = int(input())
    m = m + 1

## Memasukkan elemen" yang sudah diinput ke dalam matrix kosong
matrixKosong [0][0] = i1[0]
matrixKosong [0][1] = i1[1]
matrixKosong [0][2] = i1[2]
matrixKosong [1][0] = i1[3]
matrixKosong [1][1] = i1[4]
matrixKosong [1][2] = i1[5]
matrixKosong [2][0] = i1[6]
matrixKosong [2][1] = i1[7]
matrixKosong [2][2] = i1[8]

## Mencetak matrix sesuai elemen yg diinput (bukan matrix kosong)
print (" ")
for x1 in range(3) :
    print (matrixKosong[x1])

print("\n")


def TransposeMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

TransposeMatrix(matrixKosong)

for r in result:
    print(r)