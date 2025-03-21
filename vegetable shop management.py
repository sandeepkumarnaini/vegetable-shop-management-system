veg=['brinjal','tomato','onion','potato']
it_p=[0,0,0,0]
quantity=[50,50,50,50]
original_price=[40,35,20,30]
selling_price=[45,40,25,36]
start=0
profit=0
r=0
nam=[]
mob=[]
vegetables=[]
price=[]
qun=[]
a_m=[]
t_t=[]

while True:
    if start=='close':
        password=input('Enter Password')
        while True:
            if password=='password':
                print('Press 1 to add vegetables: ')
                print('Press 2 to remove vegetables: ')
                print('Press 3 to display vegetables: ')
                print('Press 4 to Customer Infomation: ')
                print('Press 5 to Print Report: ')
                print('Press 6 to exit')
                while True:
                    ch=int(input('choose the number: '))
                    if ch==1:
                        veg_add=input('Which vegetable you want to add: ')
                        if veg_add in veg:
                            print('vegetable is already existing: ')
                        else:
                            veg.append(veg_add)
                                            
                            qty_add=int(input('enter the quantity you want to add: '))
                            quantity.append(qty_add)
                            ori_pri=int(input('enter the original price of the vegetable:'))
                            original_price.append(ori_pri)
                            sel_pri=int(input('enter the selling price of the vegetable: '))
                            selling_price.append(sel_pri)

                                            
                    elif ch==2:
                        veg_rem=input('which vegetable you want to remove: ')
                        if veg_rem in veg:
                            ind=veg.index(veg_rem)
                            quantity.pop(ind)
                            original_price.pop(ind)
                            selling_price.pop(ind)
                            veg.remove(veg_rem)
                                            
                        else:
                            print('vegetable is not existing: ')
                    elif ch==3:
                        print('Available Items')
                        print()
                        for i in veg:
                            print(i)
                        print()    
                    elif ch==4:
                        for zz in zip(nam,mob,vegetables,price,qun,a_m,t_t):
                            print('Name :',zz[0],'    ','Mobile Number :',zz[1])
                            print()
                            print(' Items      Qunatity      P/kg        Amount')
                            for i in range(len(zz[2])):
                                print(zz[2][i],'     ',zz[4][i],' Kgs','     ',zz[3][i],' Rs P/Kg'
                                      ,'     ',zz[5][i],' Rs',sep='')
                            print(' Total ',zz[6])
                            print(20*'-')
                    elif ch==5:
                        print(10*'*','REPORT',10*'*')
                        for it in zip(veg,quantity):
                            print(it[0],'-----',it[1])
                        print()
                        print(10*'*','ITEMIZED_PROFIT',10*'*')
                        for z in zip(veg,it_p):
                            print(z[0],'----',z[1])
                        print()
                        print(10*'*','INCOME',10*'*')
                        print()
                        print('TOTAL_PROFIT: ',profit,'----','REVENUE: ',r)
                        print()
                        print(60*'*')
                    

                    elif ch==6:

                        break

                break
            else:
                print('')
            
        break
                
            
           
        #print(a_m)
        #print(t_t)
        #print(qun)
        
    '---------------------------------------------------------------------------------'
    total=0
    print('***** Available Items *****')
    for i in veg:
        print('--',i,end=' ')
    print()
    print()
    print('WELCOME')
    start=input('Do YOU Want To Start Shopping: (y/n)')
    if start=='y':
        name=input('ENTER YOUR NAME: ')
        while True:
            mob_num=(input('ENTER YOUR MOBILE NUMBER: '))
            if len(mob_num)==10:
                break
            else:
                print('enter valid mobile number')
                continue
    
        nam.append(name)
        mob.append(mob_num)
    
    
    
        v=[]
        q=[]
        p=[]
        am=[]
        tt=[]
        while True:   
            
            item=input('what do you want (type "done" to finish): ')
            print()

            if item=='done':
                print('-- THANK YOU', name.upper() ,'FOR SHOPPING WITH US --')
                print(10*'*','CUSTOMER_BILL',10*'*')
                print('Items       Quantity       Price       Amount')
                for b in zip(v,q,p,am):
                    print()
                    print(b[0],'     ',b[1],' kgs','       ',b[2],' P/kg','     ',b[3],' Rs',sep='')
                vegetables.append(v)
                price.append(p)
                qun.append(q)
                a_m.append(am)
                t_t.append(tt)
                    
                    
                print('TOTAL AMOUNT: ',total)
                
                tt.append(total)
                r=r+total
                print(60*'*')
                break
                    
            
            
            elif item in veg:
                v.append(item)
                qty=float(input('how many kgs do you want:'))
                print()
                idx=veg.index(item)
                if qty<=quantity[idx]:
                    q.append(qty)
                    p.append(selling_price[idx])
                    amount=qty*selling_price[idx]
                    am.append(amount)
                    print('AMOUNT IS: ',amount)
                    total=total+amount
                    
                    print()
                    quantity[idx]=quantity[idx]-qty
                    profit =profit+qty*(selling_price[idx]-original_price[idx])
                    it_p[idx]=it_p[idx]+qty*(selling_price[idx]-original_price[idx])
                else:
                    print('out of stock')
                    print('available stock is :',quantity[idx])
                    print()
            
            
                   
            else:
                print(item ,'is not available')
                print()    

    else:
        continue
