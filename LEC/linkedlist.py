class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr =''
        return 'Link(' + repr(self.first) + repr(self.rest) + ')'
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + ' '
    
def square(x):
    return x*x
def odd(x):
    return x%2==1
def range_link(start,end):
    if start >= end:
        return Link.empty
    else:
        return Link(start,range_link(start+1, end))

def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first),map_link(f, s.rest))
    
def filter_link(f, s):
    if s is Link.empty:
        return s
    return Link(s.first, filter_link(s.rest)) if f(s.first) else filter_link(s.rest)
