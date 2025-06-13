def main ():
   
   # 1st 3 digits tell where the user is calling from
    phone = '+1 617-495-1000' 
    
    
    print(phone[0:3]) # from 0 index to 3 index doesn't include 3rd index
    print(phone[8:]) # blank index left means all the way to the end and vice-versa 
    print(phone[-4:]) # used it bc of +1 added in phone variable


main()