# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
#
# Return the total number of provinces.
#
#
#
# Example 1:
#
#
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:
#
#
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
#
#
# Constraints:
#
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

def findCircleNum(self, M: List[List[int]]) -> int:
    # Optimized using Union by Size / Rank (Merge smaller trees to larger trees, to maintain balance and keep trees flat)
    def union(node_A, node_B):
        root_A = findRoot(node_A)
        root_B = findRoot(node_B)

        if size[root_A] < size[root_B]:
            root[root_A] = root_B
            size[root_B] += size[root_A]
        else:
            root[root_B] = root_A
            size[root_A] += size[root_B]

    # Optimized using Path Compression (Make every other node in path point to it's grandparent, keeps trees flat)
    def findRoot(node):
        if root[node] == node:
            return node

        root[node] = findRoot(root[node])

        return root[node]

    rows = len(M)
    cols = len(M[0])
    res = rows
    # Key - node , Value - size of the set/tree/component rooted at given node
    size = defaultdict(int)
    # Key - node , Value - Parent/Root node
    root = defaultdict(int)

    # Initializing root and size dicts with default values, each node is it's own root and each node has a size of 1 initially
    for studentNum in range(rows):
        root[studentNum] = studentNum
        size[studentNum] = 1

    for i in range(rows-1):
        for j in range(i+1, cols):
            if i != j and M[i][j] == 1 and findRoot(i) != findRoot(j):
                union(i, j)
                res -= 1

    return res