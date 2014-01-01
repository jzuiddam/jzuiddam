def make_table(L):
    s = ""
    for x in L:
        s += "| @%s@ | $%s$ |\n" % (x,x)
    return s
