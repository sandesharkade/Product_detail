$(document).ready(function(){
  // register ajax
  $("#register").click(function(){
    // Checking for blank fields.
    if( $("#username").val() == '' || $("#password").val()==''){
      $('input[id="username"],input[id="password"],input[id="confirm_password"]').css("border","2px solid red");
      $("#error").html("Please fill all the fields!");
    } else if($("#password").val().length < 5){
      $("#error").html("Password length should be more than 4");
    } else if( $("#confirm_password").val()!=$("#password").val()){
      $("#error").html("Passwords don't match. Try again!");
    } else {
      $.ajax({
        type: "POST",
        url:"register",
        data: $('#register_form').serialize(),
        success: function(data)
        {
          window.location = '';
        },
        error: function(data){
          $("#error").html("Username already exists!");
        }
      });
    }
  });

  //login ajax
  $("#login").click(function(){
    if( $("#u_name").val() =='' || $("#login_password").val() ==''){
      $('input[id="u_name"],input[id="login_password"]').css("border","2px solid red");
      $("#error_login").html("Please fill all the fields!");
    }  else {
      $.ajax({
        type: "POST",
        url:"/",
        data: $('#login_form').serialize(),
        success: function(data)
        {
          window.location = 'product';
        },
        error: function(data){
          $("#error_login").html("Please check username or password");
        }
      });
    }
  });
});
