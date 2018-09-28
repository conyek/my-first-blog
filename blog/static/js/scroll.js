$(document).ready(function() {
  $("#link1").click(function() {
    $path = $("#whatIdo").offset().top;
    $("body").animate({ scrollTop: $path }, 1000);
  });
  $("#link2").click(function() {
    $path = $("#work").offset().top;
    $("body").animate({ scrollTop: $path }, 1000);
  });
  $("#link3").click(function() {
    $path = $("#contact").offset().top;
    $("body").animate({ scrollTop: $path }, 1000);
  });
});
$(function() {
  $('[data-toggle="tooltip"]').tooltip();
});
