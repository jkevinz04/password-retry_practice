p = 'a123456'
count = 3 #剩餘機會
while count > 0:
    count -= 1
    password = input('請輸入密碼： ')
    if p == password:
        print('登入成功!')
        break #逃出迴圈
    else:
        if count == 0:
        	print('你沒有機會了！')
        else:
        	print('密碼錯誤!還有', count, '次機會')