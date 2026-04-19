import time

A = [0] * 10
B = [0] * 10
C = [0] * 10
D = [0] * 10
E = [0] * 10
F = [0] * 10
G = [0] * 10

numbers = [" 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8" ," 9"]

CopyValue = 0

LoopIndexB = 0
LoopIndexE = 0

CanRun = False

DoLoopF = False
DoLoopNF = False
LoopTimes = 0

Val1 = 0
Val2 = 0
Val3 = 0

index = 0

def CheckWriteREG() :
    if lineDecoder[0][0:1] == "A":
        if lineDecoder[0][1:2] == "0":
            A[int(lineDecoder[0][2:]) - 1] = int(lineDecoder[1])
        else:
            A[int(lineDecoder[0][1:]) - 1] = int(lineDecoder[1])

    if lineDecoder[0][0:1] == "B":
        if lineDecoder[0][1:2] == "0":
            B[int(lineDecoder[0][2:]) - 1] = int(lineDecoder[1])
        else:
            B[int(lineDecoder[0][1:]) - 1] = int(lineDecoder[1])

    if lineDecoder[0][0:1] == "C":
        if lineDecoder[0][1:2] == "0":
            C[int(lineDecoder[0][2:]) - 1] = int(lineDecoder[1])
        else:
            C[int(lineDecoder[0][1:]) - 1] = int(lineDecoder[1])

    if lineDecoder[0][0:1] == "D":
        if lineDecoder[0][1:2] == "0":
            D[int(lineDecoder[0][2:]) - 1] = int(lineDecoder[1])
        else:
            D[int(lineDecoder[0][1:]) - 1] = int(lineDecoder[1])

    if lineDecoder[0][0:1] == "E":
        if lineDecoder[0][1:2] == "0":
            E[int(lineDecoder[0][2:]) - 1] = int(lineDecoder[1])
        else:
            E[int(lineDecoder[0][1:]) - 1] = int(lineDecoder[1])

    if lineDecoder[0][0:1] == "F":
        if lineDecoder[0][1:2] == "0":
            F[int(lineDecoder[0][2:]) - 1] = int(lineDecoder[1])
        else:
            F[int(lineDecoder[0][1:]) - 1] = int(lineDecoder[1])

    if lineDecoder[0][0:1] == "G":
        if lineDecoder[0][1:2] == "0":
            G[int(lineDecoder[0][2:]) - 1] = int(lineDecoder[1])
        else:
            G[int(lineDecoder[0][1:]) - 1] = int(lineDecoder[1])

def CheckWriteTER() :

    if lineDecoder[1][1:2] == "A" :
        print(f"A{lineDecoder[1][2:]} :", A[int(lineDecoder[1][2:]) - 1])

    if lineDecoder[1][1:2] == "B" :
        print(f"B{lineDecoder[1][2:]} :", B[int(lineDecoder[1][2:]) - 1])

    if lineDecoder[1][1:2] == "C" :
        print(f"C{lineDecoder[1][2:]} :", C[int(lineDecoder[1][2:]) - 1])

    if lineDecoder[1][1:2] == "D" :
        print(f"D{lineDecoder[1][2:]} :", D[int(lineDecoder[1][2:]) - 1])

    if lineDecoder[1][1:2] == "E" :
        print(f"E{lineDecoder[1][2:]} :", E[int(lineDecoder[1][2:]) - 1])

    if lineDecoder[1][1:2] == "F" :
        print(f"F{lineDecoder[1][2:]} :", F[int(lineDecoder[1][2:]) - 1])

    if lineDecoder[1][1:2] == "G" :
        print(f"G{lineDecoder[1][2:]} :", G[int(lineDecoder[1][2:]) - 1])

def CheckWriteCOPY():
    global CopyValue
    if lineDecoder[1][1:2] == "A" :
        CopyValue = A[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "B" :
        CopyValue = B[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "C" :
        CopyValue = C[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "D" :
        CopyValue = D[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "E" :
        CopyValue = E[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "F" :
        CopyValue = F[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "G" :
        CopyValue = G[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "A" :
        A[int(lineDecoder[2][2:]) - 1] = CopyValue

    if lineDecoder[2][1:2] == "B" :
        B[int(lineDecoder[2][2:]) - 1] = CopyValue

    if lineDecoder[2][1:2] == "C" :
        C[int(lineDecoder[2][2:]) - 1] = CopyValue

    if lineDecoder[2][1:2] == "D" :
        D[int(lineDecoder[2][2:]) - 1] = CopyValue

    if lineDecoder[2][1:2] == "E" :
        E[int(lineDecoder[2][2:]) - 1] = CopyValue

    if lineDecoder[2][1:2] == "F" :
        F[int(lineDecoder[2][2:]) - 1] = CopyValue

    if lineDecoder[2][1:2] == "G" :
        G[int(lineDecoder[2][2:]) - 1] = CopyValue

def AddREG() :
    global Val1, Val2, Val3
    if lineDecoder[1][1:2] == "A" :
        Val1 = A[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "B" :
        Val1 = B[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "C" :
        Val1 = C[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "D" :
        Val1 = D[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "E" :
        Val1 = E[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "F" :
        Val1 = F[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "G" :
        Val1 = G[int(lineDecoder[1][2:]) - 1]

        # Val2

    if lineDecoder[2][1:2] == "A" :
        Val2 = A[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "B" :
        Val2 = B[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "C" :
        Val2 = C[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "D" :
        Val2 = D[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "E" :
        Val2 = E[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "F" :
        Val2 = F[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "G" :
        Val2 = G[int(lineDecoder[1][2:]) - 1]

    Val3 = Val1 + Val2

    if lineDecoder[3][1:2] == "A" :
        A[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "B" :
        B[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "C" :
        C[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "D" :
        D[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "E" :
        E[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "F" :
        F[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "G" :
        G[int(lineDecoder[3][2:]) - 1] = Val3

def SubREG() :
    global Val1, Val2, Val3
    if lineDecoder[1][1:2] == "A" :
        Val1 = A[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "B" :
        Val1 = B[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "C" :
        Val1 = C[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "D" :
        Val1 = D[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "E" :
        Val1 = E[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "F" :
        Val1 = F[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "G" :
        Val1 = G[int(lineDecoder[1][2:]) - 1]

        # Val2

    if lineDecoder[2][1:2] == "A" :
        Val2 = A[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "B" :
        Val2 = B[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "C" :
        Val2 = C[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "D" :
        Val2 = D[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "E" :
        Val2 = E[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "F" :
        Val2 = F[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "G" :
        Val2 = G[int(lineDecoder[1][2:]) - 1]

    Val3 = Val1 - Val2

    if lineDecoder[3][1:2] == "A" :
        A[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "B" :
        B[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "C" :
        C[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "D" :
        D[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "E" :
        E[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "F" :
        F[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "G" :
        G[int(lineDecoder[3][2:]) - 1] = Val3

def MulREG() :
    global Val1, Val2, Val3
    if lineDecoder[1][1:2] == "A" :
        Val1 = A[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "B" :
        Val1 = B[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "C" :
        Val1 = C[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "D" :
        Val1 = D[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "E" :
        Val1 = E[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "F" :
        Val1 = F[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "G" :
        Val1 = G[int(lineDecoder[1][2:]) - 1]

        # Val2

    if lineDecoder[2][1:2] == "A" :
        Val2 = A[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "B" :
        Val2 = B[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "C" :
        Val2 = C[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "D" :
        Val2 = D[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "E" :
        Val2 = E[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "F" :
        Val2 = F[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "G" :
        Val2 = G[int(lineDecoder[1][2:]) - 1]

    Val3 = Val1 * Val2

    if lineDecoder[3][1:2] == "A" :
        A[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "B" :
        B[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "C" :
        C[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "D" :
        D[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "E" :
        E[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "F" :
        F[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "G" :
        G[int(lineDecoder[3][2:]) - 1] = Val3

def DivREG() :
    global Val1, Val2, Val3
    if lineDecoder[1][1:2] == "A" :
        Val1 = A[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "B" :
        Val1 = B[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "C" :
        Val1 = C[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "D" :
        Val1 = D[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "E" :
        Val1 = E[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "F" :
        Val1 = F[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[1][1:2] == "G" :
        Val1 = G[int(lineDecoder[1][2:]) - 1]

        # Val2

    if lineDecoder[2][1:2] == "A" :
        Val2 = A[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "B" :
        Val2 = B[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "C" :
        Val2 = C[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "D" :
        Val2 = D[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "E" :
        Val2 = E[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "F" :
        Val2 = F[int(lineDecoder[1][2:]) - 1]

    if lineDecoder[2][1:2] == "G" :
        Val2 = G[int(lineDecoder[1][2:]) - 1]

    Val3 = Val1 // Val2

    if lineDecoder[3][1:2] == "A" :
        A[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "B" :
        B[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "C" :
        C[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "D" :
        D[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "E" :
        E[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "F" :
        F[int(lineDecoder[3][2:]) - 1] = Val3

    if lineDecoder[3][1:2] == "G" :
        G[int(lineDecoder[3][2:]) - 1] = Val3

userInput = input("Action : ")
userInputDec = userInput.split()

if userInputDec[0] == "Run" :
    CanRun = True
    print("\n")
    with open(userInputDec[1], "r") as file:
        lines = file.readlines()

while CanRun :
    time.sleep(0.1)

    if index >= len(lines) :
        break

    lineDecoder = lines[index].strip().split("-")

    CheckWriteREG()

    if lineDecoder[0] == "Twrite " :
        CheckWriteTER()
    
    if lineDecoder[0] == "Rcopy " :
        CheckWriteCOPY()

    if lineDecoder[0] == "Radd " :
        AddREG()

    if lineDecoder[0] == "Rsub " :
        SubREG()

    if lineDecoder[0] == "Rmul " :
        MulREG()

    if lineDecoder[0] == "Rdiv " :
        DivREG()

    if lineDecoder[0] == "loop " :
        if lineDecoder[1] == " Forever" :
            LoopIndexB = index
            DoLoopF = True
            DoLoopNF = False
        if lineDecoder[1] in numbers :
            LoopIndexB = index
            DoLoopF = False
            DoLoopNF = True
            LoopTimes = int(lineDecoder[1]) - 1

        if lineDecoder[1] == " ^^^" :
            LoopIndexE = index

    if DoLoopF and index == LoopIndexE :
        index = LoopIndexB

    if DoLoopNF and index == LoopIndexE and LoopTimes > 0:
        index = LoopIndexB
        LoopTimes -= 1

    index += 1
