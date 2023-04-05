const lightTheme = document.querySelector('#light-theme');
const darkTheme = document.querySelector('#dark-theme');
const themeToggler = document.querySelector('#theme-toggler');

themeToggler.onclick = () => {
  if (darkTheme.disabled == true) {
    // dark mode
    themeToggler.innerText = 'Light';
    darkTheme.disabled = false;
  } else {
    // light mode
    themeToggler.innerText = 'Dark';
    darkTheme.disabled = true;
  }
};
