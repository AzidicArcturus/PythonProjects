class Node:
    def __init__(self, value):
        self.l = None
        self.r = None
        self.v = value
        self.isSubtree = True

    def info(self):
        writeFormat = ("""==== NODE {0} INFO ====\n
Left value: {1}\n
Right value: {2}\n
Is it a subtree?: {3}\n
============================
"""
                      ).format(self.v, self.l, self.r, self.isSubtree)
        print(writeFormat)
                       

    
class Tree:
    def __init__(self_root, rootvalue):
        self_root.root = rootvalue
        self_root.l = None
        self_root.r = None
        self_root.v = rootvalue
        self_root.treeDatabase = {}

    def createNode(self_root, value):
        node = Node(value)
        #print("NODE V:", node.v)
        
        def _createNode(node):
            self_root.treeDatabase[node.v] = [node.l, node.r]
            
        if self_root.l == None or self_root.r == None:
            
            #print(ord(str(node.v)[0]), ord(str(self_root.v)[0]))
            
            if ord(str(node.v)[0]) >= ord(str(self_root.v)[0]) or self_root.l != None:
                if self_root.r == None:
                    self_root.r = value
                    self_root.treeDatabase[self_root.root] = [self_root.l, self_root.r]
                    _createNode(node)
                    #self_root.update({node.v:[node.l, node.r]})
                   #print(self_root.treeDatabase)
                    
            elif ord(str(node.v)[0]) < ord(str(self_root.v)[0]) or self_root.r != None:
                if self_root.l == None:
                    self_root.l = value
                    self_root.treeDatabase[self_root.root] = [self_root.l, self_root.r]
                    _createNode(node)
                    #self_root.update({node.v:[node.l, node.r]})
                    #print(self_root.treeDatabase)
                    
        if self_root.l != None and self_root.r != None:
            _createNode(node)

        x.displaytreeDatabase()


    def displaytreeDatabase(self_root):
        print("ROOT NODE DATABASE\nKEY:{nodename : [leftvalue, rightvalue]}\n" + str(self_root.treeDatabase))

    def createNodeLink(self_root, existing_node, new_node):
        new_node = Node(new_node)
        for i in list(self_root.treeDatabase.keys()):
            
            print(new_node.v, i, new_node.v == i)
            if new_node.v == i:
                self_root.treeDatabase.pop(existing_node, [new_node.l, new_node.r])
                self_root.treeDatabase.pop(new_node.v, [new_node.l, new_node.r])
                
                if ord(str(existing_node)[0]) >= ord(str(new_node)[0]) or existing_node.l != None:
                    self_root.treeDatabase[existing_node] = [new_node.v, None]
                    self_root.treeDatabase[new_node.v] = [existing_node, None]
                    
                elif ord(str(existing_node)[0]) < ord(str(new_node)[0]) or existing_node.r != None:
                    self_root.treeDatabase[existing_node] = [None, new_node.v]
                    self_root.treeDatabase[new_node.v] = [None, existing_node]
                    
        #print("SRTR", self_root.treeDatabase)
                
        

x = Tree('ROOT')
x.createNode('Azidic')
x.createNode('Molly')
x.createNode('Trevor')
x.createNodeLink('Azidic', 'Trevor')
x.createNodeLink('Trevor', 'Azidic')
x.displaytreeDatabase()


    
            
        
        
        
