$(document).ready(function() {
    $(".col-md-4").click(function(){
         window.location=$(this).find('.div-click').attr("href");
         return false;
    });
});