nis = float(input("Enter the amount in shekels: "))
dollars = nis / 3.21
rupees = nis * 0.046
print(f"The amount of {nis} shekels is equal to {dollars:.2f} dollars.")
print(f"The amount of {nis} shekels is equal to {rupees:.2f} rupees.")

additional_rupees = float(input("Enter the additional amount in rupees: "))
additional_shekels = additional_rupees / 0.046
additional_dollars = additional_shekels / 3.21
print(f"The additional amount of {additional_rupees} rupees is equal to {additional_shekels:.2f} shekels.")
print(f"The additional amount of {additional_rupees} rupees is equal to {additional_dollars:.2f} dollars.")