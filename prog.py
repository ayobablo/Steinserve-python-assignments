print('please input your home address')
address=input()

if len(address)<5:
    print ('the length of your address is less than 5')

elif len(address)<10:
    print ('the length of your address is less than 10')

elif len(address)<20:
    print ('the length of the address is less than 20')

else:
    print ('the length of your address is greater than 20')
