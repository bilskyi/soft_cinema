document.addEventListener('DOMContentLoaded', function() {
    var dropdownMenu = document.querySelector('#dropdownMenu');
    var menuItems = document.querySelectorAll('.dropdown-menu li');

    dropdownMenu.addEventListener('click', function(event) {
      event.stopPropagation();
      document.querySelector('.dropdown-menu').classList.toggle('show');
    });

    menuItems.forEach(function(item) {
      item.addEventListener('click', function(event) {
        event.stopPropagation();
      });
    });

    document.addEventListener('click', function() {
      document.querySelector('.dropdown-menu').classList.remove('show');
    });
  });