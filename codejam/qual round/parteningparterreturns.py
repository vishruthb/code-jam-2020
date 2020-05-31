def parenting_partnering_returns():
    N = input()
    intervals = sorted(map(int, raw_input().strip().split()) + [i] for i in xrange(N))
    result, c_e, j_e = [None]*N, 0, 0
    for s, e, i in intervals:
        if c_e <= s:
            c_e = e
            result[i] = 'C'
        elif j_e <= s:
            j_e = e
            result[i] = 'J'
        else:
            return "IMPOSSIBLE"
    return "".join(result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, parenting_partnering_returns())