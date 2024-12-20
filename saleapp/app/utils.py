def cal_cart(cart):
    total_counter = 0
    total_price = 0

    if cart:
        for x in cart.values():
            total_counter += x['quantity']
            total_price += x['quantity'] * x['price']

    return {'total_counter': total_counter,
            'total_price': total_price}
