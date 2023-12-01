let header = document.querySelector('header');
let toggle_header = document.querySelector('#toggle_header');
//header.classList.add('red');
toggle_header.addEventListener("click", () => {
  header.classList.toggle('red')
  header.classList.toggle('green')
});
