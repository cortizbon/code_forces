s1 = input('Primer string:' ).lower()
s2 = input('Segundo string:' ).lower()

if s1 < s2:
	print('-1')
elif s2 < s1:
	print('1')
elif s1==s2:
	print('0')
else:
	None
