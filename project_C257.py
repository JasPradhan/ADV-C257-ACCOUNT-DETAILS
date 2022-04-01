from tkinter import *
from web3 import Web3
from PIL import ImageTk, Image

root = Tk()
root.title("Account Details")
root.configure(bg="cyan")

ganache_url = 'http://127.0.0.1:7545'

web_3 = Web3(Web3.HTTPProvider(ganache_url))

img = ImageTk.PhotoImage(Image.open("image_project257.png"))
panel = Label(root, image=img, bg='cyan')
panel.pack(side="top")

frame = Frame(
    root,
    bg='cyan',
    padx=5,
    pady=5
)
# create the labels to hold the account numbers
Label(frame,text="Account number 1:",fg="blue",bg="cyan").grid(row=0,column=0,sticky="W",pady=10)
Label(frame,text="Account number 2:",fg="blue",bg="cyan").grid(row=1,column=0,sticky="W",pady=10)
Label(frame,text="Account number 3:",fg="blue",bg="cyan").grid(row=2,column=0,sticky="W",pady=10)
Label(frame,text="Account number 4:",fg="blue",bg="cyan").grid(row=3,column=0,sticky="W",pady=10)
Label(frame,text="Account number 5:",fg="blue",bg="cyan").grid(row=4,column=0,sticky="W",pady=10)


#Create entry elements to get the use input for account addresses 
account1=Entry(frame)
account2=Entry(frame)
account3=Entry(frame)
account4=Entry(frame)
account5=Entry(frame)

#place the entry elements on the root window
account1.grid(row=0,column=0,sticky="W",pady=10)
account2.grid(row=1,column=0,sticky="W",pady=10)
account3.grid(row=2,column=0,sticky="W",pady=10)
account4.grid(row=3,column=0,sticky="W",pady=10)
account5.grid(row=4,column=0,sticky="W",pady=10)

#create the text box
result=Text(root,height=10,width=45,fg="gold",bg="blue")

#define a function CHECK_BALANCE() and add the code inside it.


def CHECK_BALANCE():
	count=1
	account_no=[]
	account_no.append(account1.get())
	account_no.append(account2.get())
	account_no.append(account3.get())
	account_no.append(account4.get())
	account_no.append(account5.get())
	for i in account_no:
		balance=web_3.eth.getBalance(i)
		balance=balance*0.000000000000000001
		result.insert(END,f'Account {count} balance is : {balance} \n')
		count+=1

frame.pack()

#Create a button element to call the CHECK_BALANCE()
check_balance=Button(width=15,text="CHECK BALANCE",command=CHECK_BALANCE)
check_balance.pack(fill='both')
    

result.pack(pady=5)
root.mainloop()

