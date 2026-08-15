const addItem = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

addItem.addEventListener('click', () => {
  const listItem = document.createElement('li');

  listItem.textContent = 'Item';
  list.appendChild(listItem);
});
