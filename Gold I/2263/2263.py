import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

node = [0]*(n+1)  # 원소의 인덱스를 저장할 배열
for i in range(n):
    node[inorder[i]] = i


def preorder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return

    root = postorder[postEnd]  # 후위순회에서 마지막 원소가 최상위 루트임

    leftNode = node[root] - inStart  # 왼쪽 서브 트리 원소 개수
    rightNode = inEnd - node[root]  # 오른쪽 서브 트리 원소 개수
    # 전위 순회는 VLR 순서로 순회, root 먼저 출력 후 왼쪽 서브 트리 순회
    print(root, end=" ")
    preorder(inStart, inStart+leftNode-1, postStart,
             postStart+leftNode-1)  # 왼쪽 서브트리 순회
    preorder(inEnd-rightNode+1, inEnd, postEnd-rightNode, postEnd-1)


preorder(0, n-1, 0, n-1)
