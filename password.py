# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確   就印出 "登入成功"
# 如果不正確  就印出 "密碼錯誤! 還有_次機會!"
password = 'a123456'
x = 3 # 剩餘機會
while x >= 1:
	answer = input('請輸入密碼: ')
	if answer == password:
	    print('登入成功!')
	    break
	elif answer != password:
		x = x-1
		print('密碼錯誤! 剩餘', x,'次機會')
		