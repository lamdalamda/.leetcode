#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# @lc code=start


class Solution:
    def __init__(self):
        self.edges={}
        self.nodes=[]
        self.headnode_val=True
        self.val_to_index_dict={}
        # key=node.val value=index of the node in "node_of_newgraph"
        self.nodes_of_newgraph=[]
        
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        return self.cloneGraph1(node)
    
    
    def cloneGraph1(self, node: 'Node') -> 'Node':
        # 基本思路：寻找所有的子节点，往self.edges里面塞数据，然后再生成一个新的？
        # Node.val is unique for each node.
        
        self.headnode_val=node.val
        self.read_graph_to_edges(node)
        self.build_graph_from_edges(self.headnode_val)
        return self.nodes_of_newgraph[0]
        
        
        pass        
    
    def read_graph_to_edges(self,node):
        
        # convert the "node" format graph to list format
        
        self.edges[node.val]=[]
        
        if node.neighbors is None:
            return None
        for i in node.neighbors:
            self.edges[node.val].append(i.val)
            if i.val not in self.edges:
                self.read_graph_to_edges(i)
    
    def build_graph_from_edges(self,build_node_val=0):
        if build_node_val not in self.val_to_index_dict:
            # this node is not yet created
            self.val_to_index_dict[build_node_val]=len(self.nodes_of_newgraph)            
            self.nodes_of_newgraph.append(Node(build_node_val))  
            
            if self.edges[build_node_val]==[]:
                return None
            # if no neighbor, then is ok to return
            
            
            # initialize neighbor
            self.nodes_of_newgraph[self.val_to_index_dict[build_node_val]].neighbors=[]
                
            for i in self.edges[build_node_val]:# neighbors
                if i not in self.val_to_index_dict:
                    #this node not yet built
                    self.build_graph_from_edges(i)
                    
                self.nodes_of_newgraph[self.val_to_index_dict[build_node_val]].neighbors.append(self.nodes_of_newgraph[self.val_to_index_dict[i]])
                


        
        
                
        
        
        
# @lc code=end

