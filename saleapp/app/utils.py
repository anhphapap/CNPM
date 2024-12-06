def cal_cart(cart):
    total_amount = 0
    total_price = 0

    for x in cart.values():
        total_amount += x['quantity']
        total_price += x['quantity'] * x['price']

    return {'total_amount': total_amount,
            'total_price': total_price}
