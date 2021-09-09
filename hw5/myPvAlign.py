def myPvAlign(pv, noteVec):
    import numpy as np

    noteVec = np.array(noteVec)
    DP = [[0.0 for i in range(0, len(pv))] for j in range(0, len(noteVec))]
    DP = np.array(DP)
    pv = np.array(pv)

    for i in range(0, len(noteVec)):
        DP[i, :] = abs(pv - noteVec[i])
    for i in range(0, len(noteVec)):
        if i != 0:
            DP[i][0] = float('inf')

    for i in range(0, len(noteVec)):
        for j in range(0, len(pv)):
            if i != 0 and j == 0:
                continue
            elif i == 0 and j == 0:
                continue
            elif i == 0 and j != 0:
                DP[i][j] = DP[i][j] + DP[i][j - 1]
                continue
            DP[i][j] = DP[i][j] + min(DP[i - 1][j - 1], DP[i][j - 1])

    return min(DP[:, -1])