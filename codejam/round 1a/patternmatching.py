def pattern_matching():
    N = input()
    P = [raw_input().strip().split('*') for _ in xrange(N)]
    prefix, suffix = "", ""
    for i in xrange(N):
        if len(prefix) < len(P[i][0]):
            prefix = P[i][0]
        if len(suffix) < len(P[i][-1]):
            suffix = P[i][-1]
    for i in xrange(N):
        if not prefix.startswith(P[i][0]):
            return "*"
        if not suffix.endswith(P[i][-1]):
            return "*"
    result = [prefix]
    for i in xrange(N):
        result.extend(P[i][1:-1])
    result.append(suffix)
    return "".join(result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, pattern_matching())