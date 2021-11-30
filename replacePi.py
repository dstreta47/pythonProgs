def replacePi(string, start):
    #base case
	if len(string) < 2 or start == len(string):
		return string
        
    #recursion case
	replacePi(string, start + 1)

    #shifting
	if(string[start] == 'p' and string[start + 1] == 'i'):
		string[start:start + 2] = ['3', '.', '1', '4']




string = "pippppiiiipi"
string = list(string)
replacePi(string,0)
string = ''.join(string)
print(string)
