"""
This sum_to_n function sums integers up to n. It
store the results in a dictionary, and the function
will use the stored results to return the answer
in fewer iterations.
"""
stored_results = {}

def sum_to_n(n): 
    result = 0
    for i in reversed(range(n)):
        if i + 1 in stored_results:
            print('Stop summing at {} since we have computed it'.format(i))
            result += stored_results[i +1]
            break
        else:
            result += i + 1
    stored_results[n] = result
    return result

print(sum_to_n(8))