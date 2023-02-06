ord('あ')    #12354 #ord: 文字→コードポイント(10進数,Unicode)

chr(12354)   #あ    #chr: コードポイント→文字

Alp=[chr(ord('A')+i) for i in range(26)] # 大文字のアルファベットからなる配列
alp=[chr(ord('a')+i) for i in range(26)] # 小文字のアルファベットからなる配列
