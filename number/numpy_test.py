import numpy as np


def testing_numpy():
    """Test numpy"""
    ax = np.array([1,2,3])
    ay = np.array([1,2,3])
    print(ax)
    print(ax*2)
    print(ax+10)
    print(np.sqrt(ax))
    print(np.cos(ax))
    print(ax-ay)
    print(np.where(ax<2,ax, 10))

    m = np.matrix([ax, ay, ax])
    print(m)
    print(m.T)

    grid1 = np.zeros(shape =(10,10), dtype = float)
    # zeros 는 모든 요소를 0 으로 초기화
    # zeros(shape, dtype= float , order='C')
    grid2 = np.ones(shape=(10,10), dtype=float)
    # ones 는 모든 요소를 1로 초기화
    # ones(shape, dtype= None , order='C')
    print(grid1)
    print(grid2)
    print(grid1[1]+10)
    print(grid2[:,2]*2)
    print("-------------------")
    print(grid2[:,1]) 
    # print(grid2[:,1]) 1행만 출력하는 것 같음.

if __name__ == "__main__":
    testing_numpy()