class BurgerSamples:
    BREAD_NAME = "Краторная булка"
    BREAD_PRICE = 100
    SAUCE_NAME = "Соус"
    SAUCE_KIND = "SAUCE"
    SAUCE_PRICE = 25
    FILLING_NAME = "Начинка"
    FILLING_KIND = "FILLING"
    FILLING_PRICE = 50

    PRICE_CASES = [
        (0, BREAD_PRICE * 2),
        (1, BREAD_PRICE * 2 + SAUCE_PRICE),
        (2, BREAD_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE),
    ]
    BREAD_LINE = f"(==== {BREAD_NAME} ====)"
    RECEIPT_CASES = [
        (0, [BREAD_LINE, BREAD_LINE, "", f"Price: {BREAD_PRICE * 2}"]),
        (2, [BREAD_LINE, f"= {SAUCE_KIND.lower()} {SAUCE_NAME} =",
             f"= {FILLING_KIND.lower()} {FILLING_NAME} =", BREAD_LINE, "",
             f"Price: {BREAD_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE}"]),
    ]
