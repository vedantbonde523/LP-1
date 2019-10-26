# Demonstration of alpha-beta pruning

MAX, MIN = 1000, -1000

def minmax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):

    if depth == 3:
        return values[nodeIndex]
    
    if maximizingPlayer:

        best = MIN

        for i in range(0, 2):

            val = minmax(depth+1, nodeIndex*2 + i, False, values, alpha, beta)
            best =  max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        for i in range(0, 2):

            val = minmax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best

## Driver
if __name__ == '__main__':

    values = [2,3,5,9,0,1,7,5]
    print('The optimal value is: ', minmax(0, 0, True, values, MIN, MAX)) 
