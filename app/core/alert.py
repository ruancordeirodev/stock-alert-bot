def check_alert(symbol, price, target, mode):
    if price is None:
        return False

    if mode == "below":
        return price <= target

    if mode == "above":
        return price >= target

    return False