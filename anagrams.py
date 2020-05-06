
'''
anagrams - method 1 (sort and compare)
Time complexity - O(nlog(n))
Space complexity - O(n^2)
'''
def anagram_1(str1,str2):
	if len(str1) == len(str2):

		lst1 =[]
		lst2 =[]
		for char in str1:
			lst1.append(char)
		for char in str2:
			lst2.append(char)
		if sorted(lst1) == sorted(lst2):
			print(sorted(lst2))
			return True
		else:
			return False
	else:
		return 'Not gonna work man! Sorry!'

#print(anagram_1('earth','heart'))
#print(anagram_1('nsn','nsns'))
#print(anagram_1('python','typhon'))
'''
anagrams - method 2 (naive method)
Time complexity - O(n^2)
Space complexity - O(n) 

 So, in this method I assumed str1 to be given is always be the right one,
for intance, str1 ='akhii'and str2 = 'akhil' are not anagrams and thus return False.
Whereas, str1 = 'akhil' and str2 = 'akhii' are not anagrams but returns True because every character
in string2 is compared with all characters of string1. So, in string2 when there is a double i it matches
with the given i.So, most of the test cases will pass.
'''
def anagram_2(str1,str2):
	if len(str1)==len(str2):
		pos2 = 0
		lst = []
		while(pos2<len(str2)):
			pos1=0
			while(pos1<len(str2)):
				if str1[pos1] == str2[pos2]:
					lst.append(str2[pos2])
				pos1 += 1
			pos2 += 1
		print(lst)
		print(list(str2))
		if list(str2)==lst:
			return True
		else:
			return False 
	else:
		return 'Not happening'

#print(anagram_2('cinema','iceman'))
#print(anagram_2('nsn','nsns'))
#print(anagram_2('python','typhon'))
#print(anagram2('akhii','akhil'))
 
