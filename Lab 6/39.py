def calculate_da(basic):
    return basic * 0.40


def calculate_hra(basic):
    return basic * 0.20


def calculate_net_salary(basic):
    da = calculate_da(basic)
    hra = calculate_hra(basic)

    return basic + da + hra


basic = float(input("Enter basic pay: "))

da = calculate_da(basic)
hra = calculate_hra(basic)
net = calculate_net_salary(basic)

print("\n--- SALARY SLIP ---")
print("Basic Pay:", basic)
print("DA (40%):", da)
print("HRA (20%):", hra)
print("Net Salary:", net)
