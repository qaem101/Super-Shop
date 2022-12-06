// cart
let cartIcon = document.querySelector('#cart-icon')
let cartIcon = document.querySelector('#cart-icon')
let cartIcon = document.querySelector('#cart-icon')

// cart working
if(document.readyState == "loading"{
	document.addEventListener('DOMContentLoaded',ready);
}else{
	ready();
}

// making function
function ready(){
	// remove item from cart
	var removeCartButtons = document.getElementsByClassName('cart-remove')
	console.log(removeCartButtons)
	for(var i = 0; i < removeCartButtons.length ; i++){
		var button = removeCartButtons[i];
		button.addEventListener('click', removeCartItem)
	}
}

// Remove item fron cart
function removeCartItem(event){
	var buttonClicked = event.target
	buttonClicked.parentElement.remove()
}

// Update total
function updatetotal(){
	var cartcontent = document.getElementsByClassName('cart-content')[0]
    var cartBoxes = cartContent.getElementsByClassName('cart-box')

    for(var i = 0; cartBoxes.length ; i++){
    	var cartBox = cartBoxes[i]
    	var priceElement = cartBox.getElementsByClassName('cart-price')
    	var quantityElement
    }

}