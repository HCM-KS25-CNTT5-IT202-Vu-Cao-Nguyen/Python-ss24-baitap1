class CoffeeOrder:
    var_rate = 0.10

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0

    @property
    def total_amount(self):
        return self.__total_amount

    def add_item(self, price):
        if price > 0:
            self.__total_amount += price
        else:
            print("Giá của món phải lớn hơn 0")

    def calculate_final_bill(self):
        return self.__total_amount * (1 + CoffeeOrder.vat_rate)

    @classmethod
    def update_vat_rate(cls, new_rate):
        if 0 <= new_rate <= 1:
            cls.vat_rate = new_rate
            print(f"Đã cập nhập VAT toàn hệ thống thành {new_rate * 100:.0f}%")
        else:
            print("Mức VAT không hợp lệ")

order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

order_table1.add_item(50000)
order_table2.add_item(30000)

print("=" * 50)
print("THÔNG TIN HÓA ĐƠN BAN ĐẦU")
print("=" * 50)

print(f"{order_table1.table_number}: {order_table1.total_amount} VNĐ")
print(f"{order_table2.table_number}: {order_table2.total_amount} VNĐ")

print()


print("=" * 50)
print("THỬ GIAN LẬN")
print("=" * 50)

try:
    order_table1.total_amount = 0
except AttributeError as e:
    print("Không thể sửa tổng tiền từ bên ngoài!")
    print("Lỗi:", e)

print()
print(f"Tổng tiền {order_table1.table_number}: {order_table1.total_amount} VNĐ")

print()


print("=" * 50)
print("CẬP NHẬT VAT")
print("=" * 50)

CoffeeOrder.update_vat_rate(0.08)

print()

print(f"VAT của Bàn 1: {order_table1.vat_rate * 100:.0f}%")
print(f"VAT của Bàn 2: {order_table2.vat_rate * 100:.0f}%")

print()

print("=" * 50)
print("HÓA ĐƠN CUỐI")
print("=" * 50)

print(
    f"{order_table1.table_number}: "
    f"Tạm tính = {order_table1.total_amount} VNĐ | "
    f"Thanh toán = {order_table1.calculate_final_bill():,.0f} VNĐ"
)

print(
    f"{order_table2.table_number}: "
    f"Tạm tính = {order_table2.total_amount} VNĐ | "
    f"Thanh toán = {order_table2.calculate_final_bill():,.0f} VNĐ"
)