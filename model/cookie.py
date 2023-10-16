import random

cookie_data = {
    "cookies": [],
    "list": [
        "Chocolate Chip", "Oatmeal Raisin", "Snickerdoodle", "Peanut Butter", "Sugar Cookie"
    ]
}

# Initialize cookies
def initCookies():
    # Setup cookies into a dictionary with type, ingredients, price, and stock
    for item_type in cookie_data["list"]:
        cookie_data["cookies"].append({"type": item_type, "ingredients": [], "price": 0, "stock": 0})
    # Prime some stock levels
    for i in range(len(cookie_data["list"])):
        cookie_data["cookies"][i]["stock"] = random.randint(50, 100)

# Return all cookies from cookie_data
def getCookies():
    return cookie_data["cookies"]

# Cookie getter
def getCookie(cookie_type):
    for cookie in cookie_data["cookies"]:
        if cookie['type'] == cookie_type:
            return cookie

# Return random cookie from cookie_data
def getRandomCookie():
    return random.choice(cookie_data["cookies"])

# Buy a cookie and update stock
def buyCookie(cookie_type):
    cookie = getCookie(cookie_type)
    if cookie and cookie['stock'] > 0:
        cookie['stock'] -= 1
        return {"message": f"Purchased one {cookie_type} cookie."}
    elif cookie:
        return {"message": f"Sorry, {cookie_type} cookies are out of stock."}, 400
    else:
        return {"message": "Cookie type not found."}, 404

# Pretty Print cookie
def printCookie(cookie):
    print("Type:", cookie['type'])
    print("Ingredients:", ', '.join(cookie['ingredients']))
    print("Price:", cookie['price'])
    print("Stock:", cookie['stock'])

# Number of cookies
def countCookies():
    return len(cookie_data["cookies"])

# Test Cookie Model
if __name__ == "__main__":
    initCookies()  # initialize cookies

    # Random cookie
    random_cookie = getRandomCookie()
    print("Random cookie:")
    printCookie(random_cookie)

    # Buy a cookie
    cookie_type = "Chocolate Chip"  # Change to the type you want to buy
    buy_result = buyCookie(cookie_type)
    print(buy_result)

    # Count of Cookies
    print("Cookies Count:", countCookies())
