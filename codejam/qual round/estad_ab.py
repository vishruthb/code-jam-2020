from sys import stdout

def flip(arr):
  return [x^1 for x in arr]

def reverse(arr):
  return arr[::-1]

def query(i, count):
    print i+1 if i is not None else 1
    stdout.flush()
    return input(), count+1

def check(result):
    print "".join(map(str, result))
    stdout.flush()
    ok = raw_input().strip()
    if ok != "Y":  # error
        exit()

def esab_atad():
    result, count, flip_i, reverse_i = [0]*B, 0, None, None
    for i in xrange(B//2):
        if count and count%10 == 0:
            flip_res, count = query(flip_i, count)
            reverse_res, count = query(reverse_i, count)
            if flip_i is not None and (result[flip_i]^flip_res):
                result = flip(result)
            if reverse_i is not None and (result[reverse_i]^reverse_res):
                result = reverse(result)
        result[i], count = query(i, count)
        result[B-i-1], count = query(B-i-1, count)
        if result[i] == result[B-i-1]:
            flip_i = i
        else:
            reverse_i = i
    check(result)

T, B = map(int, raw_input().strip().split())
for case in xrange(T):
    esab_atad()