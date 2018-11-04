$(document).ready(function(){
  $('.header').height($(window).height());
  $('.pdf_summarize').height($(window).height() - $('.navbar').height() - 15);
  $('.type_in_to_summarize').height($(window).height() - $('.navbar').height() - 15);


  $(".navbar a").click(function(){
 	$("body,html").animate({
 		scrollTop:$("#" + $(this).data('value')).offset().top - ($('.navbar').height() + 15)
 	},800)
 })

  $("#btn_summarize_pdf").click(function() {
  	console.log($("#" + $(this).data('value')).offset().top); 
  	$("body,html").animate({
 		scrollTop:$("#" + $(this).data('value')).offset().top - ($('.navbar').height() + 15)
 	},800)
  })

  $("#btn_type_in_to_summarize").click(function() {
  	$("body,html").animate({
 		scrollTop:$("#" + $(this).data('value')).offset().top - ($('.navbar').height() + 15)
 	},800)
  })

  /*$(function() {
    $('#btn_submit_text').click(function() {
        $.ajax({
            url: '/summarizeText',
            data: $('#text_submit_form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log("success!");
                $('#response').text(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
  });
*/

  $('#btn_submit_text').on('click', function(e) {
        e.preventDefault(); 
        $.ajax({
            url: '/summarizeText',
            data: $('#text_submit_form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                $('#response').text(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

})

