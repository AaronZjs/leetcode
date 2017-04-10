#coding:utf-8

"""

给出二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7


返回其自底向上的层次顺序遍历:

[
  [15,7],
  [9,20],
  [3]
]


"""


tree = [3,9,20,None,None,15,7]

#反转树
tree.reverse()
ntree = []

# 反序组合枝叶
for i in range(len(tree)):
	if(i%2) == 0:
		if i+1 < len(tree):
			if tree[i] == None and tree[i+1] == None:
				pass
			elif tree[i] != None and tree[i+1] != None:
				ntree.append([tree[i+1],tree[i]])
			elif tree[i] == None and tree[i+1] != None:
				ntree.append([tree[i+1]])
			elif tree[i] != None and tree[i+1] == None:
				ntree.append([tree[i]])
		else:
			if tree[i] == None:
				pass
			else:
				ntree.append([tree[i]])

print ntree