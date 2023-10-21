function toggleDropdown() {
    var dropdownMenu = document.getElementById("dropdownMenu");
    if (dropdownMenu.style.display === "none") {
        dropdownMenu.style.display = "block";
    } else {
        dropdownMenu.style.display = "none";
    }
}
// Hàm JavaScript để chuyển đổi giỏ hàng
function toggleCart() {
    var cart = document.getElementById('cart');
    if (cart.style.display === 'none') {
        cart.style.display = 'block';
    } else {
        cart.style.display = 'none';
    }
}

// Thêm một trình lắng nghe sự kiện vào nút giỏ hàng
var cartButton = document.querySelector('.btn-outline-primary');
cartButton.addEventListener('click', toggleCart);

document.addEventListener("DOMContentLoaded", function() {
    const cartButton = document.getElementById("cart-button");
    const searchForm = document.querySelector(".search-form form");

    cartButton.addEventListener("click", function(event) {
      event.preventDefault();  // Ngăn chặn form submission
      window.location.href = searchForm.getAttribute("action");  // Điều hướng đến URL của form
    });
  });