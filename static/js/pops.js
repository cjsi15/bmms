$(document).ready(function(){
  $(".borrow").click(function(){
  	 $(".intro").hide();
  	 $(".col-sm-4").show();
  	 $('.table').show();
  	  $(".borrowee").show();
  	  $('.formstock').hide();
  	  $('.form-table').hide();
  	  $('.bg-secondary').hide();
  	  $('.navbar-nav').hide();
  });
   $(".addstocks").click(function(){
  	 $(".intro").hide();
  	 $(".col-sm-4").hide();
  	 $('.table').hide()
  	 $('.formstock').show();
  	 $('.form-table').show();
  	 $('.bg-secondary').show();
  	 $('.intro').hide();
  	 $(".borrowee").hide();
  	 $('.navbar-nav').hide();
  });
});
