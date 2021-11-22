
def get_max(sub):
    print(max(sub))
    return ord(max(sub))
test_list = ["gs", "is", "best", "for", "cs"]
test_list.sort(key=get_max)
print(str(test_list))
      
