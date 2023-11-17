class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        print(f"{self.name} {quantity}잔의 가격은 {total_price}원입니다.")


Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)


selected_beverage = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")
if selected_beverage in ["커피", "녹차", "아이스티"]:
    quantity = int(input("수량을 입력하세요: "))
    if quantity > 0:
        if selected_beverage == "커피":
            Coffee.calculate(quantity)
        elif selected_beverage == "녹차":
            GreenTea.calculate(quantity)
        elif selected_beverage == "아이스티":
            IceTea.calculate(quantity)
        else:
            print("올바른 음료를 선택하세요.")
    else:
        print("수량은 1 이상이어야 합니다.")
else:
    print("올바른 음료를 선택하세요.")
