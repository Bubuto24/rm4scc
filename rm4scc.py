def rm4scc(postal_code: str) -> str:
	sTbl = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	iTop = iBot = 0
	for char in postal_code:
		find_char = sTbl.find(char)
		if find_char != -1:
			iTop += (find_char // 6) + 1
			iBot += (find_char % 6) + 1
		else:
			return postal_code + "?"
	# Offset row and column by 1
	return postal_code + sTbl[6 * ((iTop - 1) % 6) + ((iBot - 1) % 6)]


print(rm4scc("BX11LT1A"))
