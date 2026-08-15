document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');
  const list = document.querySelector('.my_list');

  addItem.addEventListener('click', () => {
    const listItem = document.createElement('li');

    listItem.textContent = 'Item';
    list.appendChild(listItem);
  });

  removeItem.addEventListener('click', () => {
    if (list.lastElementChild !== null) {
      list.removeChild(list.lastElementChild);
    }
  });

  clearList.addEventListener('click', () => {
    while (list.firstChild !== null) {
      list.removeChild(list.firstChild);
    }
  });
});
