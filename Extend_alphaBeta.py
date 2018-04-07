import math

def minimax(depth, nodeindex, boolmax, values, alpha, beta):
    if depth == 3:
        return values[nodeindex]
    if boolmax:
        best = Min
        if depth == 0:
            lenght = len(values)
            if lenght >8:
                ln = math.ceil(lenght/4)
                for i in range(ln):
                    val = minimax(depth + 1, nodeindex * 2 + i, False, values, alpha, beta)
                    best = max(best, val)
                    alpha = max(alpha, best)
                    # alpha beta pruning.
                    if beta <= best:
                        break
        for i in range(2):
            val = minimax(depth+1,nodeindex*2+i,False,values,alpha,beta)
            best = max(best,val)
            alpha = max(alpha,best)
            #alpha beta pruning.
            if beta <= best:
                break
        return best
    else:
        best = Max
        for i in range(2):
            val = minimax(depth+1,nodeindex*2+i,True,values,alpha,beta)
            best = min(best,val)
            beta = min(beta,best)
            # alpha beta pruning.
            if best <= alpha:
                break
        return best


Max = 1000
Min = -1000


if __name__ == '__main__':

    #values =[4,6,7,9,1,2,0,1,8,1,9,2]  #8
    #values = [3,5,6,9,1,2,0,-1]     #5
    #values = [7,5,6,9,2,5,3,1,8,-1]

    print("Test case number: ", end='')
    x = eval(input())
    for i in range(x):
        print("Enter values : ", end='')
        values = [int(x) for x in input().split()]
        print("The optimal value of Alpha Beta pruning is :",minimax(0, 0, True, values, Min, Max))
