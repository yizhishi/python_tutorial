# CalBMI.py

height, weight = eval ( input ('输入身高, 体重: '))

bmi = weight /pow(height, 2)
#print('BMI 是: {:.2f}'.format(bmi))

who, nat = "", ""
if bmi < 18.5:
    who, nat = "瘦", "瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
else:
    who, nat = "胖", "胖"
print('BMI指数为, 国际: {}, 国标: {}'.format(who, nat))
