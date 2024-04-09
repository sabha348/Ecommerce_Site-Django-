const submitButton = document.querySelector('#btn-submit');
const submitButtonText = document.querySelector('#btn-submit .button-text');

submitButton.addEventListener('click', (e) => {
//e.preventDefault();
  
  submitButton.classList.add('loading');
  
  setTimeout(() => {
    submitButton.classList.remove('loading');
    submitButton.classList.add('success');
    submitButtonText.innerHTML = 'Login Successful';
    document.getElementById('form').sumbit();
  }, 4000);
  
});

$(document).ready(function() {
  setTimeout(function() {
      $('.alert').fadeOut('fast');
  }, 5000); // <-- time in milliseconds, 5000 ms = 5 sec
});
