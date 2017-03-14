def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE     
    
    M = L[::-1]
    d = {}
    i = 0
    
    for m in M:
        d[i] = m
        i+=1    

    def polysum(x):        
        psum = 0        
        for k in d.keys():
            psum += d[k]*x**k
        return psum

    return polysum