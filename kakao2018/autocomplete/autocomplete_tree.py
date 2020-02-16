class Node:
    def __init__(self, char):
        self.character = char
        self.cnt = 1
        self.children = []

def insert(root , word):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.character == char:
#                print(char + " found!")
                child.cnt += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
#            print(char + "not found! --> create " + char + "node!")
            new_node = Node(char)
            node.children.append(new_node)
            node = new_node

def sum(node):
    total = 0
#    print("[ Node ] : " + node.character + " " + str(node.cnt))
    for child in node.children:
#        print("--> " + child.character + " " + str(child.cnt))
        if child.cnt == 1 :
            total += 1
        else :
            total += sum(child) + child.cnt
    return total

def solution(words):
    answer = 0

    root = Node('*')

    for word in words:
#        print("[ Insert " + word + " ]")
        insert(root, word)

    answer = sum(root)
    
    print("[ " + str(answer) + " ]")
    return answer


if __name__ == "__main__":
    words = ["go", "gone", "guild"]
    answer = 7
    if solution(words) == answer:
        print("PASS")
    else:
        print("FAIL")