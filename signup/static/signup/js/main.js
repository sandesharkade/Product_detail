// When DOM is ready
$(document).ready(function(){

// Launch MODAL BOX if the Login Link is clicked
$("#login_button").click(function(){
$('#myModal').modal();
});

// When the form is submitted
$("#status > form").submit(function(){

// Hide 'Submit' Button
$('#submit').hide();

// 'this' refers to the current submitted form
var str = $(this).serialize();

// -- Start AJAX Call --

$.ajax({
    type: "POST",
    url: "{% url login_url  %}",  // Send the login info to this page
    data: str,
  success: function(msg){
    msg='';

$("#status").ajaxComplete(function(event, request, settings){

 // Show 'Submit' Button
$('#submit').show();

 if(msg == '') // LOGIN OK?
 {
 var login_response = '<div id="logged_in">' +
	 '<div style="width: 350px; float: left; margin-left: 70px;">' +
	 '<div style="width: 40px; float: left;">' +
	 '<img style="margin: 10px 0px 10px 0px;" align="absmiddle" src="images/ajax-loader.gif">' +
	 '</div>' +
	 '<div style="margin: 10px 0px 0px 10px; float: right; width: 300px;">'+
	 "You are successfully logged in! <br /> Please wait while you're redirected...</div></div>";

$('a.modalCloseImg').hide();

$('#simplemodal-container').css("width","500px");
$('#simplemodal-container').css("height","120px");

 $(this).html(login_response); // Refers to 'status'

// After 3 seconds redirect the
setTimeout('go_to_private_page()', 1000);
 }
 else // ERROR?
 {
 var login_response = msg;
 $('#login_response').html(login_response);
 }

 });

 }

  });

// -- End AJAX Call --

return false;

}); // end submit event

});

function go_to_private_page()
{
window.location = 'private.php'; // Members Area
}
