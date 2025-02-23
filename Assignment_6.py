def sym_diff(s, t):
    return (s.difference(t)).union(t.difference(s))
