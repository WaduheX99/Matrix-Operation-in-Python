matrix1 = []
i1 = [0] * (9)
operasi = [0] * (3)
dt = 0

## Membuat matrix kosong 3x3
for x1 in range(3) :
    matrix1.append([])
    for y1 in range(3) :
        matrix1[x1].append(0)

## Menginputkan elemen" matrix
m = 0
for x in range(0, 8 + 1, 1):
    print("masukkan elemen ke - " + str(x + 1))
    i1[m] = int(input())
    m = m + 1

## Memasukkan elemen" yang sudah diinput ke dalam matrix kosong
matrix1 [0][0] = i1[0]
matrix1 [0][1] = i1[1]
matrix1 [0][2] = i1[2]
matrix1 [1][0] = i1[3]
matrix1 [1][1] = i1[4]
matrix1 [1][2] = i1[5]
matrix1 [2][0] = i1[6]
matrix1 [2][1] = i1[7]
matrix1 [2][2] = i1[8]

## Mencetak matrix sesuai elemen yg diinput (bukan matrix kosong)
print (" ")
for x1 in range(3) :
    print (matrix1[x1])

operasi[0] = matrix1[0][0] * (matrix1[1][1] * matrix1[2][2] - matrix1[2][1] * matrix1[1][2])
operasi[1] = matrix1[0][1] * (matrix1[1][0] * matrix1[2][2] - matrix1[2][0] * matrix1[1][2])
operasi[2] = matrix1[0][2] * (matrix1[1][0] * matrix1[2][1] - matrix1[2][0] * matrix1[1][1])
dt = operasi[0] - operasi[1] + operasi[2]

## Output jawaban determinan
print (" ")
print ("jadi determinan matrix yang diinput adalah : ")
print (dt)
