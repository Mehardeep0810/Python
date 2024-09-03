mydict={'First_name':'Mehardeep','Last_name':'Kaur','Roll_no':'2210997287','Age':'19','Phone_no':'8544182652','Email':'mehardeep@gmail.com','City':'Patiala','State':'Punjab','Stream':'BCA','University':'Chitkara University'}
print('===============================================================')
print('{:<15}\t||\t {:<15}'.format('Key','Value'))
print('===============================================================')
for key,value in mydict.items():
    print('{:<15}\t||\t {:<15}'.format(key,value))
print('===============================================================')
print('Total Records : ',len(mydict))
print('===============================================================')
