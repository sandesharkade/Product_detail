$(document).ready(function(){
  // register ajax
  $("#register").click(function(){
    // COAhecking for blank fields.
    if( $("#username").val() == '' || $("#password").val()==''){
      $('input[id="username"],input[id="password"],input[id="confirm_password"],input[id="email"]').css("border","2px solid red");
      $("#error").html("Please fill all the fields!");
    } else if($("#password").val().length < 5){
      $("#error").html("Password length should be more than 4 characters");
    } else if( $("#confirm_password").val()!=$("#password").val()){
      $("#error").html("Passwords don't match.");
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

         if(data.responseText=="usernameemail")
          {
            $("#error").html("Username already exists and Invalid email address.");
          }
          else if(data.responseText=="email")
          {
            $("#error").html("Invalid email address.");
          }
          else
          {
            $("#error").html("Username already exists.");
          }
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
