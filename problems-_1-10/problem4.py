#classification tree for animals
#Binary tree will be constructed to store the conditions to better model the classification
# A method on the ClassificationTree class will print all the data in the tree in an inorder manner
#The data in each node will hold the question to be asked use a loop!



class TreeNode:
    def __init__(self,data,left=None,right=None) -> None:
        self.data=data
        self.left=left
        self.right=right

class ClassificationTree:
    def __init__(self,head):
        self.head=head
 
   

def build_tree():
    tree=ClassificationTree(TreeNode("Is the animal a mammal? "))
    head=tree.head
    head.right=TreeNode("Is it domesticated? ")
    print(type(head.right))
    head.right.left=TreeNode("Does it live at the ocean")
    head.right.right=TreeNode("Do we ride it? ")
    head.right.left.left=TreeNode("Are its children called cubs")
    head.right.left.right= TreeNode("Is it the largest mammal on earth? ")
    head.right.right.left= TreeNode( "Is its meat called lamb or mutton? ")
    head.right.right.right= TreeNode("Your animal is a horse")
    head.right.left.left.left=TreeNode("Your animal is a tiger")
    head.right.left.left.right=TreeNode("Your animal is a lion")
    head.right.left.right.left=TreeNode( "Is your animal the smartest animal on the planet? ")
    head.right.left.right.right= TreeNode("Your animal is a whale")
    head.right.right.left.left= TreeNode("Is your animal a cow")
    head.right.right.left.right= TreeNode("Your animal is a sheep")
    head.right.left.right.left.left= TreeNode("Your animal is a seal")
    head.right.left.right.left.right= TreeNode("Your animal is a dolphin")
    head.right.right.left.left.left= TreeNode("Your animal is a pig")
    head.right.right.left.left.right= TreeNode("Your animal is a cow")


    head.left=TreeNode("Is the animal a bird? ")
    head.left.left= TreeNode("Is your animal an insect? ")
    head.left.right= TreeNode("Can it fly? ")
    head.left.left.left= TreeNode("Does it live underwater? ")
    head.left.left.right=TreeNode("Can it fly? ")
    head.left.right.left=TreeNode("Does it live in Antarctica? ")
    head.left.right.right= TreeNode("Your animal is a sparrow")
    head.left.left.left.left= TreeNode("Your animal is a spider")
    head.left.left.left.right= TreeNode("Does it have 8 tentacles? ")
    head.left.left.right.left= TreeNode("Your animal is an ant")
    head.left.left.right.right= TreeNode("Can it sting? ")
    head.left.right.left.left= TreeNode("Your animal is an ostritch")
    head.left.right.left.right =TreeNode("Your animal is an penguin")
    head.left.left.left.right.left= TreeNode("Your animal is a squid")
    head.left.left.left.right.right= TreeNode("Your animal is an octopus")
    head.left.left.right.right.left=TreeNode( "Your animal is a Termite")
    head.left.left.right.right.right=TreeNode("Can your animal sting twice? ")
    head.left.left.right.right.right.left=TreeNode( "Your animal is a Bee")
    head.left.left.right.right.right.right= TreeNode("Your animal is a wasp")
    
    return tree



if __name__ =='__main__':
    tree=build_tree()
    cur_node=tree.head
    while cur_node.data[0] !='Y':
        print(cur_node.data,end="  ")
        desicion=input("format= Y/N  ")
        while desicion.upper()!='Y' and desicion.upper() != 'N':
            print("Please use Y/N to show whether the question was true or false")
            desicion=input("format= Y/N  ")
        if desicion.upper()=='Y':
            print("Hi")
            cur_node=cur_node.right
        else:
            cur_node=cur_node.left
    print(cur_node.data)
    
    
