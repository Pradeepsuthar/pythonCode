// popover cart
$('#displatCart').popover()
document.getElementById("displatCart").setAttribute('data-content','Vivamus sagittis lacus vel <b>augue</b> laoreet rutrum faucibus.')

// find cart items from localstoarge
if (localStorage.getItem('cart') == null) {
    var cart = {};
}
else {
    cart = JSON.parse(localStorage.getItem('cart'));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
}

// increament cart items in cart on btn clicked
$('.cart').click(function () {
    var idstr = this.id.toString();
    if (cart[idstr] != undefined) {
        cart[idstr] = cart[idstr] + 1;
    }
    else {
        cart[idstr] = 1;
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
});



// calculations



