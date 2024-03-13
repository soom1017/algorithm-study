# 골드 3
# Trie 자료구조
# 참고: https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8A%B8%EB%9D%BC%EC%9D%B4-Trie

import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, foods):
        cur_node = self.root

        for food in foods:
            if food not in cur_node.children:
                cur_node.children[food] = Node() # children에 해당 food가 없는 경우 추가해줌
            cur_node = cur_node.children[food] # 다음 노드로 이동
        
        cur_node.children[0] = None # leaf임을 나타냄
    
    @staticmethod
    def print_trie(cur_node: Node, depth):
        if 0 in cur_node.children:
            return

        node_list = sorted(cur_node.children)

        for node in node_list:
            print("--" * depth, end="")
            print(node)

            Trie.print_trie(cur_node.children[node], depth + 1)

trie = Trie()

for _ in range(int(input())):
    foods = input().split()[1:]
    trie.insert(foods)

Trie.print_trie(trie.root, 0)