import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

node = [0]*(n+1)  # ������ �ε����� ������ �迭
for i in range(n):
    node[inorder[i]] = i


def preorder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return

    root = postorder[postEnd]  # ������ȸ���� ������ ���Ұ� �ֻ��� ��Ʈ��

    leftNode = node[root] - inStart  # ���� ���� Ʈ�� ���� ����
    rightNode = inEnd - node[root]  # ������ ���� Ʈ�� ���� ����
    # ���� ��ȸ�� VLR ������ ��ȸ, root ���� ��� �� ���� ���� Ʈ�� ��ȸ
    print(root, end=" ")
    preorder(inStart, inStart+leftNode-1, postStart,
             postStart+leftNode-1)  # ���� ����Ʈ�� ��ȸ
    preorder(inEnd-rightNode+1, inEnd, postEnd-rightNode, postEnd-1)


preorder(0, n-1, 0, n-1)
