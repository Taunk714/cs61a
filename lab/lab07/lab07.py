""" Lab 07: Generators, Linked Lists, and Trees """

# Generators
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    # # method 1
    # for i in s:
    #     yield i * k

    # method 2
    yield from s * k



# Linked Lists

def link_to_list(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    # interative solution
    # path = []
    # while link:
    #     path.append(link.first)
    #     link = link.rest
    # return path
        
    # recursive solution
    path = []
    def recursive_list_to_link(link):
        if link:
            path.append(link.first)
            recursive_list_to_link(link.rest)

    recursive_list_to_link(link)
    return path
        


# Trees

def cumulative_sum(t):
    """Mutates t so that each node's label becomes the sum of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    def sum_tree(t):
        if t.is_leaf():
            return t.label
        else:
            return t.label + sum([sum_tree(branch) for branch in t.branches])
    t.label = sum_tree(t)
    for branch in t.branches:
        branch.label = sum_tree(branch)






def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    "*** YOUR CODE HERE ***"
    # def bst_min(t):
    #     if t.is_leaf():
    #         return t.label
    #     elif len(t.branches) > 2:
    #         return inf
    #     elif len(t.branches) == 2:
    #         if t.branches[0] <= t.label and t.branches[1] >= t.label:
    #             return 
    #         return min(t.label,bst_min(t.branches[0]))
    # def bst_max(t):
    #     if t.is_leaf():
    #         return t.label
    #     else:
    #         return max(t.label,bst_max(t.branches[-1]))


    # if not t.branches:
    #     return True
    # else:
    #     branch = t.branches
    #     if len(branch) == 2:
    #         if t.label >= bst_max(branch[0]) and t.label <= bst_min(branch[1]):
    #             return is_bst(branch[0]) and is_bst(branch[1])
    #         else:
    #             False
    #     elif len(branch) == 1:
    #         if t.label >= bst_max(branch[0]) or t.label <= bst_min(branch[0]):
    #             return is_bst(branch[0])
    #         else:
    #             return False
    #     else:
    #         return False



    # def bst(t,min_bst = -inf,max_bst = inf):
    #     if not t:
    #         True
    #     else:
    #         if t.label < min_bst or t.label > max_bst:
    #             return False
    #         else:
    #             return 
    # def bst(t,min_bst = -inf,max_bst = inf):
    #     if t.is_leaf():
    #         return True
    #     else:
    #         branch = t.branches
    #         if len(branch) > 2:
    #             return False
    #         elif len(branch) < 2:
    #             if branch[0].label > t.label:
    #                 return False
    #             else:
    #                 return  is_bst(branch[0])
    #         else:
    #             if branch[0].label > t.label or branch[1].label < t.label:
    #                 return False
    #             else:
    #                 return is_bst(branch[0]) and is_bst(branch[1])

    #     if t.label < bst_min(t.branches[0]) or t.label > bes_max(t.branches[1:]):
    #         return False
    #     else:
    #         is_bst()
    # i=0
    def bst(t, min_bst = -float("inf"), max_bst = float("inf")):
        # nonlocal i
        # i=i+1
        # print(i, min_bst, max_bst)
        if t.is_leaf():
            if t.label < min_bst or t.label > max_bst:
                return False
            else:
                return True
        else:
            length = len(t.branches)
            if t.label < min_bst or t.label > max_bst:
                # print(i, "大小不对")
                return False
            if length > 2:
                # print(i, "枝数不对")
                return False
            elif length == 1:
                if t.branches[0].label <= t.label:
                    # print(i,"1个，判断为左，边界是", min_bst,t.label)
                    return bst(t.branches[0], min_bst, t.label)
                else:
                    # print(i,"1个，判断为右，边界是", t.label,max_bst)
                    return bst(t.branches[0], t.label, max_bst)
            elif length == 2: 
                # print(i, "2个","左边界是", min_bst,t.label,max_bst)
                return bst(t.branches[0], min_bst, t.label) and bst(t.branches[1], t.label, max_bst)

    return bst(t)








# Link List Class
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
# Tree ADT

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()