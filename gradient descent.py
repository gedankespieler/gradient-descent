def gradient_descent(del_Q, w1, w2):
    w = [[w1, w2]]
    j = 0
    n = 0.01
    
    try:
        while not del_Q(w[j]) == 0:
            w[j].append([w[j][0] - del_Q(w[j])[0], w[j][1] - del_Q(w[j])[1]])
            j = j + 1
    except:
        w.append([0, 0])
        while not del_Q(w[j]) == 0:
            w.append([w[j][0] - del_Q(w[j])[0], w[j][1] - del_Q(w[j])[1]])
            j = j + 1
            if j > 100:
                break

    print(j)

def del_Q(w):
    return [w[0], w[1]]


if __name__ == "__main__":
    w1 = 1
    w2 = 0

    gradient_descent(del_Q, w1, w2)
