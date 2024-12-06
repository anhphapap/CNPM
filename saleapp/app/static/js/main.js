function addToCart(id, name, price){
    fetch("/api/add-cart",{
        method: 'post',
        body: JSON.stringify({
            "id": id,
            "name": name,
            "price": price
        }),
        headers: {
            "Content-Type" : "application/json"
        }
    }).then(res => res.json()).then(data => {
        let btn = document.getElementById('cart-counter');
        btn.innerText = data.total_amount;
    });
}