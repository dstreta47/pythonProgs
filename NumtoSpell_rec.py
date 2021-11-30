def NumtoSpell(n):
    word = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    if n==0:
        return
    digit = n%10    
    print(word[digit])    
    NumtoSpell(n//10)


    return


n=1765
NumtoSpell(n)        
