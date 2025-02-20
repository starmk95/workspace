document.getElementById('shippingForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const selectedShipping = document.querySelector('input[name = "shipping"]:checked').value;

    const message = `선택한 배송 방법: ${selectedShipping}`;
    document.getElementById('message').innerHTML = message;
});