// js file
function addToCart(item){
    addItemId += 1;
    var selectedItem = document.createElement('div');
    selectedItem.classList.add('cartImg');
    var img = document.createElement('img');
    img.seAttribute('src'.item.children[0].currentSrc);
    selectedItem.seAttribute('id',addItemId);
    var cartItems = document.getElementById('title');
    selectedItem.append(img);
    cartItems.append(selectedItem);
}