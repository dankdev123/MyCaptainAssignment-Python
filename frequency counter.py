from collections import Counter
test_str = "Mississippi"
  

all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
test_str.sort()
print ("count character :\n "
                                        +  str(all_freq))
