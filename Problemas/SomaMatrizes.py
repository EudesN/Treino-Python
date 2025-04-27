A = [[1, 2], [3, 4]]

B = [[5, 6], [7, 8]]

def somarMatrizes(A, B):
    X = []
    for i in  range(len(A)):
        linha = []
        for j in range(len(A[0])):
            linha.append(A[i][j] + B[i][j])
        X.append(linha)
    return X

def subtraiMatrizes(A, B):
    Y = []
    for i in range(len(A)):
        linha = []
        for j in range(len(A[0])):
            linha.append(A[i][j] - B[i][j])
        Y.append(linha)
    return Y

C = somarMatrizes(A, B)
D = subtraiMatrizes(A, B)

for linha in C:
    print(linha)

print("-"*20)

for linha in D:
    print(linha)

