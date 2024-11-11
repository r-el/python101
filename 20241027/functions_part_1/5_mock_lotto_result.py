import random

def mock_lotto_result():
    main_numbers = random.sample(range(1, 37), 6)
    strong_number = random.randint(1, 7)
    print(f"Main numbers: {sorted(main_numbers)}")
    print(f"Strong number: {strong_number}")

# call the function
mock_lotto_result()