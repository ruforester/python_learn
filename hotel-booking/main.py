import pandas as pd

df = pd.read_csv("005 hotels.csv", dtype={"id":str})
print(df)
df_cards = pd.read_csv("005 cards.csv", dtype=str).to_dict(orient="records")
print(df_cards)
df_card_security = pd.read_csv("005 card-security.csv", dtype=str)
print(df_card_security)


class Hotel:
    def __init__(self, id) -> None:
        self.id = id
        self.name = df.loc[df["id"] == self.id, "name"].squeeze()
    def avaliable(self):
        avaliability = df.loc[df["id"] == self.id, "available"].squeeze()
        if avaliability == "yes":
            return True
        return False
    def book(self):
        df.loc[df["id"] == self.id, "available"] = "no"
        df.to_csv("005 hotels.csv", index=False)

class ReservationTicket:
    def __init__(self, customer_name, hotel) -> None:
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        content = f"""
            Your booking data:
            Name: {self.customer_name}
            Hotel: {self.hotel.name}
        """
        return content
    

class CreditCard:
    def __init__(self, number) -> None:
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, "holder": holder, "cvc": cvc}
        return card_data in df_cards


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security["number"] == self.number, "password"].squeeze()
        return password == given_password
    

hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.avaliable():
    cc = SecureCreditCard("1234567890123456")
    if cc.validate(holder="JOHN SMITH", expiration="12/26", cvc="123"):
        if cc.authenticate("mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())
        else:
            print("Auth failed")
    else:
        print("Card invalid")
else:
    print("Hotel not avaliable")
