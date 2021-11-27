from textwrap import wrap
wordList = ["ab", "bc", "cd"] #WordList สามารถแก้ไขเพิ่มเติมได้ 
target = "abcd" #Target สามารถแก้ไขเพิ่มเติมได้ 

split_target = wrap(target, 2)
list_output = [a for a in wordList if a in split_target] #List Compiharsion
if len(list_output) >= 2 :
	print("Target :",target)
	print("Output :",tuple(list_output))
else:
	print("Target :",target)
	print('Output : None') 
