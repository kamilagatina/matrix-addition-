#На вход программе подаются два натуральных числа 
#n и m — количество строк и столбцов в матрицах, 
#затем элементы первой матрицы, 
#затем пустая строка, 
#далее следуют элементы второй матрицы
n,m = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
x = input()
matrix2 = [[int(i) for i in input().split()] for _ in range(n)]
matrix = [[matrix1[i][j]+matrix2[i][j] for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end = ' ')
    print()
#The program receives two natural numbers as input
#n and m are the number of rows and columns in matrices,
#then the elements of the first matrix,
#then an empty string,
#followed by the elements of the second matrix