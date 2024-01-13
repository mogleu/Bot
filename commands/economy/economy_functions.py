import json
from commands.economy.economy import mainshop, intervals

async def open_account(user):
    users = await get_bank_data()
    
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 0
        users[str(user.id)]['bank'] = 0
        
    with open("./commands/economy/bank.json", "w") as f:
        json.dump(users, f)
    return True

async def get_bank_data():
    with open("./commands/economy/bank.json", "r") as f:
        users = json.load(f)
    return users

async def update_bank(user, amount=0, mode="wallet"):
    users = await get_bank_data()
        
    users[str(user.id)][mode] += amount
    
    with open("./commands/economy/bank.json", "w") as f:
        json.dump(users, f)
    
    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
    return bal

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break
    
    if name_ == None:
        return [False,1]
    
    cost = price*amount
    
    users = await get_bank_data()
    
    bal = await update_bank(user)
    
    if bal[0]<cost:
        return [False,2]
    
    
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        
    
    with open("./commands/economy/bank.json","w") as f:
        json.dump(users, f)
    
    await update_bank(user,cost*-1,"wallet")
    
    return [True,"Worked"]

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break
    
    if name_ == None:
        return [False,1]
    
    cost = price*amount
    
    users = await get_bank_data()
    
    bal = await update_bank(user)
    
    
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    
    
    with open("./commands/economy/bank.json","w") as f:
        json.dump(users, f)
    
    await update_bank(user, cost, "wallet")
    
    return [True,"Worked"]

def display_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        total = seconds // count
        value = int(total)
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])


def setup(bot):
    pass