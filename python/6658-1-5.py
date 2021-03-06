import numpy as np;

Mat = np.matrix([
                [0, 0.5, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0.5, 0, 0, 0, 0, 0, 0],
                [0, 0.5, 0, 0, 0, 0.5, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0.5, 0, 0],
                [0, 0, 0, 0, 0, 0.5, 0, 0.333333, 0],
                [0, 0, 0.5, 0, 0.5, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0.333333, 0],
                [0, 0, 0, 0, 0.5, 0, 0.5, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0.333333, 0],
                ])

_Mat = np.matrix([
                 [0, 0.5, 0, 0, 0, 0, 0, 0],
                 [0.5, 0, 0, 0, 0.5, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0.5, 0, 0],
                 [0, 0, 0, 0, 0.5, 0, 0.333333, 0],
                 [0, 0.5, 0, 0.5, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0.333333, 0],
                 [0, 0, 0, 0.5, 0, 0.5, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0.333333, 0],
                 ])

H = (np.eye(8) - np.transpose(_Mat))
H = H.I*np.ones((8, 1))

print(np.transpose(_Mat))
print(H)

## 6

P = np.matrix([
              [0, 0.25, 0, 0.5],
              [0.5, 0, 0.3333333, 0],
              [0, 0.75, 0, 0.5],
              [0.5, 0, 0.666666667, 0]
              ])

print(P*P*P*P*P*P*P*P*P*P*P*P*P*P*P*P*P*P)
print(P*P*P*P*P*P*P*P*P*P*P*P*P*P*P*P*P*P*P)