from tkinter import ttk
from tkinter import *
import tkinter.messagebox

import psycopg2

class Shop:
    def __init__(self, root):
        
        self.root = root
        self.root.title('Shopping System')
        
        ##### VARIABLES #####
        self.userFullname = StringVar()
        self.userNickname = StringVar()
        self.userAge = IntVar()
        self.itemName = StringVar()
        self.itemPrice = DoubleVar()
        self.itemQuantity = IntVar()
        self.orderQuantity = IntVar()
        self.userFullnameOrders = StringVar()
        self.newStockQty = IntVar()

        ##### MAIN LABEL FRAME - USERS, ITEMS AND PLACE ORDERS #####
        self.mainFrame = LabelFrame(self.root, text = 'REGISTRATION')
        self.mainFrame.grid(row = 0, column = 0)

        
        ##### FIRST LABEL FRAME - USERS #####        
        self.userRegisterFrame = LabelFrame(self.mainFrame, text = 'User Register')
        self.userRegisterFrame.grid(row = 0, column = 0)

        #Info
        Label(self.userRegisterFrame, text = 'Fullname').grid(row = 0, column = 0)
        Entry(self.userRegisterFrame, textvariable = self.userFullname).grid(row = 0, column = 1)        

        Label(self.userRegisterFrame, text = 'Username').grid(row = 1, column = 0)
        Entry(self.userRegisterFrame, textvariable = self.userNickname).grid(row = 1, column = 1)

        Label(self.userRegisterFrame, text = 'Age').grid(row = 2, column = 0)
        Entry(self.userRegisterFrame, textvariable = self.userAge).grid(row = 2, column = 1)

        #Save User Button
        ttk.Button(self.userRegisterFrame, text = 'Save' , command = self.saveUserData).grid(row = 3, column = 0)

        
        ##### SECOND LABEL FRAME - PRODUCTS REGISTRATION #####
        self.itemsFrame = LabelFrame(self.mainFrame, text = 'Products Register')
        self.itemsFrame.grid(row = 0, column = 1)

        #Entries
        Label(self.itemsFrame, text = "Product's name").grid(row = 0, column = 0)
        Entry(self.itemsFrame, textvariable = self.itemName).grid(row = 0, column = 1)

        Label(self.itemsFrame, text = 'Price').grid(row = 1, column = 0)
        Entry(self.itemsFrame, textvariable = self.itemPrice).grid(row = 1, column = 1)
        
        Label(self.itemsFrame, text = 'Quantity').grid(row = 2, column = 0)
        Entry(self.itemsFrame, textvariable = self.itemQuantity).grid(row = 2, column = 1)

        #Save Product Button
        ttk.Button(self.itemsFrame, text = 'Save Product', command = self.saveItemData).grid(row = 3, column = 0)        

        
        ##### THIRD LABEL FRAME - USERS INFO #####
        #Label frame
        self.usersInfoFrame = LabelFrame(self.root, text = 'CLIENTS AND PRODUCTS')
        self.usersInfoFrame.grid(row = 3, column = 0, sticky = W+E)
        #Treeview for users
        self.usersTree = ttk.Treeview(self.usersInfoFrame, height = 5, columns = (1,2,3,4))
        self.usersTree.grid(row = 0, column = 0)
        self.usersTree.column('#0', width = 50, minwidth = 50, anchor = CENTER)
        self.usersTree.column('#1', width = 200, minwidth = 50, anchor = CENTER)
        self.usersTree.column('#2', width = 100, minwidth = 50, anchor = CENTER)
        self.usersTree.column('#3', width = 200, minwidth = 50, anchor = CENTER)
        self.usersTree.column('#3', width = 200, minwidth = 50, anchor = CENTER)

        self.usersTree.heading('#0', text = 'ID', anchor = CENTER)
        self.usersTree.heading('#1', text = 'Fullname', anchor = CENTER)
        self.usersTree.heading('#2', text = 'User name', anchor = CENTER)
        self.usersTree.heading('#3', text = 'Age', anchor = CENTER)
        self.usersTree.heading('#4', text = 'Date Registered', anchor = CENTER)

        
        ##### FOURTH LABEL FRAME - UPDATE STOCK #####
        self.updateStockFrame = LabelFrame(self.usersInfoFrame, text = 'UPDATE STOCK')
        self.updateStockFrame.grid(row = 0, column = 3)
        Label(self.updateStockFrame, text = 'New Quantity').grid(row = 0, column = 0)
        Entry(self.updateStockFrame, textvariable = self.newStockQty).grid(row = 0, column = 1)
        ttk.Button(self.updateStockFrame, text = 'Update', command = self.updateStockQty).grid(row = 1, column = 0)


        ##### FIFTH LABEL FRAME - BUTTONS #####
        self.actionsLabelFrame = LabelFrame(self.root, text = 'ACTIONS')
        self.actionsLabelFrame.grid(row = 4, column = 0, sticky = W+E)

        #Buttons
        ttk.Button(self.actionsLabelFrame, text = 'Delete User', command = self.deleteUser).grid(row = 0, column = 0)
        ttk.Button(self.actionsLabelFrame, text = 'Refresh Users List', command = self.refreshUsersList).grid(row = 0, column = 1)
        ttk.Button(self.actionsLabelFrame, text = 'Delete Product', command = self.deleteProduct).grid(row = 0, column = 2)   
        ttk.Button(self.actionsLabelFrame, text = 'Refresh Products List', command = self.refreshProductsList).grid(row = 0, column = 3)
        
        #Treeview for items
        self.itemsTree = ttk.Treeview(self.usersInfoFrame, height = 5, columns = (1,2,3))
        self.itemsTree.grid(row = 0, column = 1)
        
        self.itemsTree.column('#0', width = 50, minwidth = 50, anchor = CENTER)
        self.itemsTree.column('#1', width = 200, minwidth = 50, anchor = CENTER)
        self.itemsTree.column('#2', width = 100, minwidth = 50, anchor = CENTER)
        self.itemsTree.column('#3', width = 100, minwidth = 50, anchor = CENTER)        

        self.itemsTree.heading('#0', text = 'ID', anchor = CENTER)
        self.itemsTree.heading('#1', text = "Product", anchor = CENTER)
        self.itemsTree.heading('#2', text = 'Price', anchor = CENTER)
        self.itemsTree.heading('#3', text = 'Quantity', anchor = CENTER)            
        
        
        ##### FOURTH LABEL FRAME - PLACE ORDER #####
        self.ordersFrame = LabelFrame(self.usersInfoFrame, text = 'PLACE ORDERS')
        self.ordersFrame.grid(row = 0, column = 2)
        Label(self.ordersFrame, text = 'Quantity').grid(row = 0, column = 0)
        Entry(self.ordersFrame, textvariable = self.orderQuantity).grid(row = 0, column = 1)        
        
        ttk.Button(self.ordersFrame, text = 'Place Order', command = self.placeOrder).grid(row = 1, column = 0)


        ##### FIFTH LEVEL FRAME - SELECT ORDERS FROM ONE USER #####
        self.oneOrderFrame = LabelFrame(self.root, text = 'SELECT ORDERS FROM ONE USER')
        self.oneOrderFrame.grid(row = 1, column = 0)

        #Select all the orders from one user
        Label(self.oneOrderFrame, text = "Client's Fullname").grid(row = 1, column = 0)
        Entry(self.oneOrderFrame, textvariable = self.userFullnameOrders).grid(row = 1, column = 1)
        #Buttons
        ttk.Button(self.oneOrderFrame, text = 'Select Active Orders', command = self.ordersFromUser).grid(row = 1, column = 3)
        ttk.Button(self.oneOrderFrame, text = 'Refresh Orders', command = self.refreshOrders).grid(row = 2, column = 0)
        ttk.Button(self.oneOrderFrame, text = 'Cancel Order', command = self.cancelOrder).grid(row = 2, column = 1)
        ttk.Button(self.oneOrderFrame, text = 'Fulfill Order', command = self.fulfilledOrders).grid(row = 2, column = 2)       
        ttk.Button(self.oneOrderFrame, text = 'See Fulfilled Orders', command = self.seeFulfilledOrders).grid(row = 2, column = 3)
       
        ##### SIXTH LABEL FRAME - ORDERS QUERIES #####
        self.queriesFrame = LabelFrame(self.root, text = 'ORDERS')
        self.queriesFrame.grid(row = 2, column = 0, sticky = W+E)
        #Treeview
        self.ordersTree = ttk.Treeview(self.queriesFrame, height = 15, columns = (1,2,3,4,5,6))
        self.ordersTree.grid(row = 2, column = 0)
        self.ordersTree.column('#0', width = 250, minwidth = 200, anchor = CENTER)
        self.ordersTree.column('#1', width = 250, minwidth = 200, anchor = CENTER)
        self.ordersTree.column('#2', width = 250, minwidth = 200, anchor = CENTER)
        self.ordersTree.column('#3', width = 250, minwidth = 200, anchor = CENTER)
        self.ordersTree.column('#4', width = 250, minwidth = 200, anchor = CENTER)
        self.ordersTree.column('#5', width = 250, minwidth = 200, anchor = CENTER)           
        self.ordersTree.column('#5', width = 250, minwidth = 200, anchor = CENTER)

        self.ordersTree.heading('#0', text = "Customer's Name", anchor = CENTER)
        self.ordersTree.heading('#1', text = 'Client ID', anchor = CENTER)
        self.ordersTree.heading('#2', text = 'Product', anchor = CENTER)
        self.ordersTree.heading('#3', text = 'Price $', anchor = CENTER)
        self.ordersTree.heading('#4', text = 'Quantity', anchor = CENTER)
        self.ordersTree.heading('#5', text = 'Product ID', anchor = CENTER)
        self.ordersTree.heading('#6', text = 'DATE', anchor = CENTER)
       
        

        #Automatic methods calls
        self.getUsers()
        self.getItems()
        self.getOrders()    
        
    def postgresModifyer(self, query, args = ()):
        connector = psycopg2.connect(
            dbname = 'yourdatabase',
            user = 'postgres',
            password = 'yourpassword',
            host = 'localhost',
            port = '5432'
        )
        cursor = connector.cursor()
        cursor.execute(query, args)        

        connector.commit()
        connector.close()
        print('Succesfull Query')        

    def postgresQuery(self, query):
        connector = psycopg2.connect(
            dbname = 'yourdatabase',
            user = 'postgres',
            password = 'yourpassword',
            host = 'localhost',
            port = '5432'
        )
        cursor = connector.cursor()

        result = cursor.execute(query)
        row = cursor.fetchall()

        connector.commit()
        connector.close()
        print('Succesfull Query')
        return row   


    def saveUserData(self):
        name = self.userFullname.get()
        nickname = self.userNickname.get()
        age = self.userAge.get()
        if(len(name) != 0 and len(nickname) != 0 and age > 0):
            query = 'INSERT INTO clients(name, user_name, age) VALUES (%s, %s, %s);'
            args = (name, nickname, age)
            self.postgresModifyer(query, args)
            self.getUsers()
        else:
            tkinter.messagebox.showwarning('Wrong Input', 'One or more fields are not quite right. Please verify them.')

    def saveItemData(self):
        name = self.itemName.get()
        price = self.itemPrice.get()
        qty = self.itemQuantity.get()
        if(len(name) != 0 and price >= 0 and qty > 0):
            query = 'INSERT INTO items(name, price, quantity) VALUES(%s, %s, %s);'
            args = (name, price, qty)
            self.postgresModifyer(query, args)
            self.getItems()
        else:
            tkinter.messagebox.showwarning('Wrong Input','One or more fields are not quite right. Please verify them.')

    def placeOrder(self):
        try:
            self.usersTree.item(self.usersTree.selection())['values'][0]#Check name
            self.itemsTree.item(self.itemsTree.selection())['values'][0]#Check the id
        except IndexError as e:
            tkinter.messagebox.showwarning('Selection Error','No clients or items selected')
            return 
        clientId = self.usersTree.item(self.usersTree.selection())['text']
        itemId = self.itemsTree.item(self.itemsTree.selection())['text']
        desiredQty = self.orderQuantity.get()

        #Get the quantity from the selected row
        query1 = f'SELECT quantity FROM items WHERE item_id = {itemId};'
        stockQty = self.postgresQuery(query1)[0][0] #Select just the first item from the first tuple
        #Check for correct values
        if(stockQty == 0):
            tkinter.messagebox.showwarning('Out os stock', 'The current item is out of stock')
        elif(desiredQty == 0):            
            tkinter.messagebox.showwarning('No items selected', f'Please, select an amount greater than 0 or less than or equal to: {stockQty}')            
        elif(desiredQty > stockQty):
            tkinter.messagebox.showwarning('Stock problem','Not enough items in stock')            
        else:
            #print(f'User:{userId}, Item:{itemId}')
            query2 = 'INSERT INTO orders(clientID, itemID, quantity) VALUES(%s, %s, %s); '
            args2 = (clientId, itemId, desiredQty)
            self.postgresModifyer(query2, args2)
            difference = stockQty - desiredQty
            query3 = 'UPDATE items SET quantity = %s WHERE item_id = %s;'
            args = (difference, itemId)
            self.postgresModifyer(query3, args)            
            self.getOrders()
            self.getItems()

    def cancelOrder(self):
        try:
            self.ordersTree.item(self.ordersTree.selection())['values'][0]            
        except IndexError as e:
            tkinter.messagebox.showwarning('Nothing Selected','Please, select an order before cancelling')
            return
        answer = tkinter.messagebox.askquestion('Verification','Are you sure you want to cancel?')
        if(answer == 'yes'):
            clientId = self.ordersTree.item(self.ordersTree.selection())['values'][0]
            itemId = self.ordersTree.item(self.ordersTree.selection())['values'][4]
            qty = self.ordersTree.item(self.ordersTree.selection())['values'][3]        
            date = self.ordersTree.item(self.ordersTree.selection())['values'][5]
            #Take the original quantity, minus the ordered one and put it back
            query1 = f"SELECT quantity FROM orders WHERE itemID = {itemId} AND clientID = {clientId} AND ordered_at = '{date}';"
            orderedQuantity = self.postgresQuery(query1)[0][0]

            query2 = f'SELECT quantity FROM items WHERE item_id = {itemId};'
            stockQuantity = self.postgresQuery(query2)[0][0]        
            updatedQuantity = orderedQuantity + stockQuantity

            query3 = f'UPDATE items SET quantity = {updatedQuantity} WHERE item_id = {itemId};'
            self.postgresModifyer(query3)

            query4 = f"DELETE FROM orders WHERE clientID = {clientId} and itemID = {itemId} AND ordered_at = '{date}';"
            self.postgresModifyer(query4)
            self.getOrders()
            self.getItems()
        
    def fulfilledOrders(self):
        try:
            self.ordersTree.item(self.ordersTree.selection())['values'][0]            
        except IndexError as e:
            tkinter.messagebox.showwarning('Nothing Selected','Please, select an order before cancelling')
            return
        clientId = self.ordersTree.item(self.ordersTree.selection())['values'][0]
        itemId = self.ordersTree.item(self.ordersTree.selection())['values'][4]
        qty = self.ordersTree.item(self.ordersTree.selection())['values'][3]
        date = self.ordersTree.item(self.ordersTree.selection())['values'][5]
        #Insert the fulfilled order in the corresponding table
        query = f'INSERT INTO fulfilled_orders(clientID, itemID, quantity) VALUES({clientId},{itemId},{qty});'
        self.postgresModifyer(query)

        query2 = f"DELETE FROM orders WHERE clientID = {clientId} AND itemID = {itemId} AND ordered_at = '{date}';"
        self.postgresModifyer(query2)

        self.getOrders()
        top = Toplevel()
        top.title('Fulfilled Orders')
        #Label frame
        self.fulfilledOrdersFrame = LabelFrame(top, text = 'FULFILLED ORDERS')
        self.fulfilledOrdersFrame.grid(row = 0, column = 0)

        #Treeview
        self.fulfilledOrdersTree = ttk.Treeview(self.fulfilledOrdersFrame, height = 10, columns = (1,2,3,4))
        self.fulfilledOrdersTree.grid(row = 0, column = 0)
        self.fulfilledOrdersTree.column('#0', width = 150, minwidth = 100, anchor = CENTER)
        self.fulfilledOrdersTree.column('#1', width = 150, minwidth = 100, anchor = CENTER)
        self.fulfilledOrdersTree.column('#2', width = 150, minwidth = 100, anchor = CENTER)
        self.fulfilledOrdersTree.column('#3', width = 150, minwidth = 100, anchor = CENTER)
        self.fulfilledOrdersTree.column('#4', width = 150, minwidth = 100, anchor = CENTER)
        
        self.fulfilledOrdersTree.heading('#0', text = 'Client ID', anchor = CENTER)
        self.fulfilledOrdersTree.heading('#1', text = 'Fullname', anchor = CENTER)
        self.fulfilledOrdersTree.heading('#2', text = 'Product ID', anchor = CENTER)
        self.fulfilledOrdersTree.heading('#3', text = 'Product', anchor = CENTER)
        self.fulfilledOrdersTree.heading('#4', text = 'Fulfilled At', anchor = CENTER)

        query2 = """SELECT clients.client_id, clients.name, items.item_id, items.name, fulfilled_at
                    FROM clients
                    INNER JOIN fulfilled_orders
                        ON clients.client_id = fulfilled_orders.clientID
                    INNER JOIN items
                        ON items.item_id = fulfilled_orders.itemID;"""
        buffer = self.postgresQuery(query2)
        for i in buffer:
            self.fulfilledOrdersTree.insert('', 0, text = i[0], values = i[1:])        

    def seeFulfilledOrders(self):
        top = Toplevel()
        top.title('Fulfilled Orders')
        #Label frame
        self.fulfilledOrdersFrame = LabelFrame(top, text = 'FULFILLED ORDERS')
        self.fulfilledOrdersFrame.grid(row = 0, column = 0)

        #Treeview
        self.fulfilledOrdersTree = ttk.Treeview(self.fulfilledOrdersFrame, height = 10, columns = (1,2,3,4))
        self.fulfilledOrdersTree.grid(row = 0, column = 0)
        self.fulfilledOrdersTree.column('#0', width = 150, minwidth = 100, anchor = CENTER)
        self.fulfilledOrdersTree.column('#1', width = 150, minwidth = 100, anchor = CENTER)
        self.fulfilledOrdersTree.column('#2', width = 150, minwidth = 100, anchor = CENTER)
        self.fulfilledOrdersTree.column('#3', width = 150, minwidth = 100, anchor = CENTER)
        self.fulfilledOrdersTree.column('#4', width = 150, minwidth = 100, anchor = CENTER)
        
        self.fulfilledOrdersTree.heading('#0', text = 'Client ID', anchor = CENTER)
        self.fulfilledOrdersTree.heading('#1', text = 'Fullname', anchor = CENTER)
        self.fulfilledOrdersTree.heading('#2', text = 'Product ID', anchor = CENTER)
        self.fulfilledOrdersTree.heading('#3', text = 'Product', anchor = CENTER)
        self.fulfilledOrdersTree.heading('#4', text = 'Fulfilled At', anchor = CENTER)

        query2 = """SELECT clients.client_id, clients.name, items.item_id, items.name, fulfilled_at
                    FROM clients
                    INNER JOIN fulfilled_orders
                        ON clients.client_id = fulfilled_orders.clientID
                    INNER JOIN items
                        ON items.item_id = fulfilled_orders.itemID;"""
        buffer = self.postgresQuery(query2)
        for i in buffer:
            self.fulfilledOrdersTree.insert('', 0, text = i[0], values = i[1:])

    def ordersFromUser(self):
        name = self.userFullnameOrders.get()
        if(len(name) != 0):
            treeInfo = self.ordersTree.get_children()
            for i in treeInfo:
                self.ordersTree.delete(i)
            query = """ SELECT clients.name AS Client, client_id, items.name As Product, items.price AS Price, orders.quantity, items.item_id, ordered_at
                        FROM items
                        INNER JOIN orders
                            ON items.item_id = orders.itemID
                        INNER JOIN clients
                            ON clients.client_id = orders.clientID
                        WHERE clients.name LIKE '%{}%'
                        ORDER BY orders.ordered_at DESC;""".format(name)
            buffer = self.postgresQuery(query)
            for i in buffer:
                self.ordersTree.insert('', 0, text = i[0], values = i[1:]) 
        else:
            tkinter.messagebox.showwarning('Empty field','Please, before searching enter a name.')         
    

    def refreshOrders(self):
        self.getOrders()

    def refreshUsersList(self):
        self.getUsers()

    def refreshProductsList(self):
        self.getItems()

    def deleteUser(self):
        try:
            self.usersTree.item(self.usersTree.selection())['values'][0] 
            self.usersTree.item(self.usersTree.selection())['text']
        except IndexError as e:
            tkinter.messagebox.showwarning('Nothing Selected', 'Please, before deleting select one user')
            return
        answer = tkinter.messagebox.askquestion('Deletion', 'Are you sure you want to DELETE this user?')
        if(answer == 'yes'):
            name = self.usersTree.item(self.usersTree.selection())['values'][0]
            myId = self.usersTree.item(self.usersTree.selection())['text']
            query = 'DELETE FROM clients WHERE name = %s AND client_id = %s;'
            args = (name, myId)
            self.postgresModifyer(query, args)        
            self.getUsers()
            self.getOrders()
    
    def deleteProduct(self):
        try:
            self.itemsTree.item(self.itemsTree.selection())['values'][0]
            self.itemsTree.item(self.itemsTree.selection())['text']
        except IndexError as e:
            tkinter.messagebox.showwarning('Nothing Selected', 'Please, before deleting select one item')
            return
        answer = tkinter.messagebox.askquestion('Deletion', 'Are you sure you want to DELETE this item?')
        if(answer == 'yes'):
            name = self.itemsTree.item(self.itemsTree.selection())['values'][0]
            myId = self.itemsTree.item(self.itemsTree.selection())['text']
            query = 'DELETE FROM items WHERE name = %s AND item_id = %s;'
            args = (name, myId)
            self.postgresModifyer(query, args)
            self.getItems()
            self.getOrders()

    #### UPDATES #####
    def updateStockQty(self):
        newQty = self.newStockQty.get()
        if(newQty < 0):
            tkinter.messagebox.showwarning('Wrong Quantity', 'Please, type a valid quantity')
        else:
            try:
                self.itemsTree.item(self.itemsTree.selection())['values'][0]
            except IndexError as e:
                tkinter.messagebox.showwarning('Nothing Selected', 'Please, before updating select one item')
                return   
            itemId = self.itemsTree.item(self.itemsTree.selection())['text']                 
            query = f'UPDATE items SET quantity = {newQty} WHERE item_id = {itemId};'            
            self.postgresModifyer(query)
            self.getItems()                                    

    ##### GETTERS #####
    def getUsers(self):
        treeInfo = self.usersTree.get_children()
        for i in treeInfo:
            self.usersTree.delete(i)
        query = 'SELECT client_id, name, user_name, age, registered FROM clients ORDER BY name DESC;'
        buffer = self.postgresQuery(query)
        for i in buffer:
            self.usersTree.insert('', 0, text = i[0], values = i[1:])

    def getItems(self):
        treeInfo = self.itemsTree.get_children()
        for i in treeInfo:
            self.itemsTree.delete(i)
        query = 'SELECT item_id, name, price, quantity FROM items ORDER BY name DESC;'
        buffer = self.postgresQuery(query)
        for i in buffer:
            self.itemsTree.insert('', 0, text = i[0], values = i[1:])
    
    def getOrders(self):
        treeInfo = self.ordersTree.get_children()
        for i in treeInfo:
            self.ordersTree.delete(i)
        query = """ SELECT clients.name AS Client, client_id, items.name As Product, items.price AS Price, orders.quantity, items.item_id, ordered_at
                    FROM items
                    INNER JOIN orders
                        ON items.item_id = orders.itemID
                    INNER JOIN clients
                        ON clients.client_id = orders.clientID
                    ORDER BY orders.ordered_at DESC;"""
        buffer = self.postgresQuery(query)
        for i in buffer:
            self.ordersTree.insert('', 0, text = i[0], values = i[1:])
        

if __name__ == '__main__':
    root = Tk()
    root.resizable(False, False)
    Shop(root)

    root.mainloop()