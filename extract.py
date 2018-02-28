#!/usr/bin/env python3
import sys
from functools import reduce

error_data = None
error_result = None

schemes = ['http://','https://','file:///']
just_last = False
just_first = False

def do_extract(s,scheme):
    next_url = s.rfind(scheme.encode('utf8'))
    if next_url == -1:
        return -1
    part = s[next_url:]
    end_of_url = part.find('\x00'.encode('utf8'))
    this_url = None
    this_url=part[:end_of_url].decode('latin-1')
    return [this_url,next_url]

results = None

for f in sys.argv[1:]:
    with open(f,'rb') as t:
        data=t.read()
        results=[]
        for scheme in schemes:
            s = data
            r = do_extract(s,scheme)
            if just_last:
                if r != -1:
                    results.append(r)
            else:
                while r != -1:
                    results.append(r)
                    s=s[:r[1]]
                    try:
                        r=do_extract(s,scheme)
                    except:
                        error_data = s
                        error_result = r
                        print("Error in file: " + f)
                        exit(1)
        if just_last:
            results = [reduce((lambda x,y: x if x[1]>y[1] else y), results)[0]]
        else:
            if just_first:
                results = [reduce((lambda x,y: x if x[1]<y[1] else y), results)[0]]
            else:
                results = [x[0] for x in results]
        print('\n'.join(results))

