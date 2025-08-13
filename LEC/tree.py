def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches[tree]:
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)
    
def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)],[])
    
def increment_leaves(t):
    '''return a tree like t but every leaf incremented'''
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t),bs)
    
def increment(t):
    '''return a tree with every node incremented'''
    return tree(label(t) + 1,[increment(b) for b in branches(t)])

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-1),fib_tree(n-2)
        return tree(label(left)+label(right),[left,right])
    
def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves for b in branches(t)])
    
    