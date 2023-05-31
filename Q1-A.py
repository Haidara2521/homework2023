List1 = ['HTTP','HTTPS','FTP','DNS']
List2 = [80,443,20,53]

dictionary = {List1[i]: List2[i] for i in range(len(List1))}

print(dictionary)
