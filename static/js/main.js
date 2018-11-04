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


  $('#btn_submit_pdf').on('click', function(e) {
        e.preventDefault(); 
        $.ajax({
            url: '/summarizePDF',
           // data: $('#pdf_submit_form').serialize(),
            data: new FormData($('#pdf_submit_form')),
            type: 'POST',

            cache: false,
            contentType: false,
            processData: false,

            xhr: function() {
                var myXhr = $.ajaxSettings.xhr();
                if (myXhr.upload) {
                    // For handling the progress of the upload
                    myXhr.upload.addEventListener('progress', function(e) {
                        if (e.lengthComputable) {
                            $('progress').attr({
                                value: e.loaded,
                                max: e.total,
                            });
                        }
                    } , false);
                }
                return myXhr;
            }
            
            success: function(response) {
                console.log("success!");
                $('#response_pdf').text(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });



})

