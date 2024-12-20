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
         update(data)
    });
}

function update(data){
    let items = document.getElementsByClassName("cart-counter");
    for (let item of items)
        item.innerText = data.total_counter;

    let amounts = document.getElementsByClassName("cart-price");
    for (let item of amounts)
        item.innerText = data.total_price.toLocaleString();
}

function updateCart(product_id, obj){
   fetch(`/api/carts/${product_id}`, {
        method: "put",
        body: JSON.stringify({
            quantity: obj.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(res => res.json()).then(data => {
        update(data);
    })
}

function deleteCart(productId) {
    if (confirm("Bạn chắc chắn xóa không?") === true) {
        fetch(`/api/carts/${productId}`, {
            method: "delete"
        }).then(res => res.json()).then(data => {
            update(data);

            document.getElementById(`cart${productId}`).style.display = "none";
        })
    }
}

function pay() {
    if (confirm("Bạn chắc chắn thanh toán không?") === true) {
        fetch('/api/pay', {
            method: 'post'
        }).then(res => res.json()).then(data => {
            if (data.status === 200) {
                alert("Thanh toán thành công!");
                location.reload();
            }
        })
    }
}
