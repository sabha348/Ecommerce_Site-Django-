$(document).ready(function(){
    $('.form-control, #form2Example3c').on('keyup change', function() {
      var empty = false;
      $('.form-control').each(function() {
        if ($(this).val() == '') {
          empty = true;
        }
      });

      if (empty || !$('#form2Example3c').is(':checked')) {
        $('#registerButton').attr('disabled', 'disabled');
      } else {
        $('#registerButton').removeAttr('disabled');
      }
    });
  });



$(document).ready(function(){
  // Load any form data from localStorage
  if (localStorage.getItem('form_data')) {
    var form_data = JSON.parse(localStorage.getItem('form_data'));
    $('#id_username').val(form_data.username);
    $('#id_email').val(form_data.email);
    $('#id_password1').val(form_data.password1);
    $('#id_password2').val(form_data.password2);
  }

  // Save form data to localStorage when the form fields are changed
  $('.form-control').change(saveFormData);

  // Also save form data to localStorage when the form is submitted
  $('form').submit(saveFormData);

  // Save form data to localStorage when the page is about to be unloaded
  $(window).on('beforeunload', saveFormData);

  function saveFormData() {
    var form_data = {
      'username': $('#id_username').val(),
      'email': $('#id_email').val(),
      'password1': $('#id_password1').val(),
      'password2': $('#id_password2').val()
    };
    localStorage.setItem('form_data', JSON.stringify(form_data));
  }
});
