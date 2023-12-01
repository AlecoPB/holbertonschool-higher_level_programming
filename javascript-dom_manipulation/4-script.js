let addItem = document.querySelector('#add_item');

addItem.addEventListener('click', () => {
  let newLi = document.createElement('li');
  
  newLi.textContent = 'Item';
  
  let myList = document.querySelector('.my_list');
  
  myList.appendChild(newLi);
});
