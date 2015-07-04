/*
 * jQuery File Upload Plugin JS Example 8.9.1
 * https://github.com/blueimp/jQuery-File-Upload
 *
 * Copyright 2010, Sebastian Tschan
 * https://blueimp.net
 *
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/MIT
 */

/* global $, window */
$(function () {
    'use strict';

    var source   = $("#upload-file-template").html();
    var template = Handlebars.compile(source);

    // Initialize the jQuery File Upload widget:
    $('#fileupload').fileupload({
        // Uncomment the following to send cross-domain cookies:
        //xhrFields: {withCredentials: true},
        dropZone: $(".upload_box"),
        autoUpload: false
    });

    $("#fileupload")
        .bind('fileuploadadd', function(e, data){
            $.each(data.files, function (index, file) {
                console.log('Added file: ' + file.name);
                
                var context = {filename: file.name};
                $(".upload_area").append(template(context));
                       

            });
        })
        .bind('fileuploadchange', function(e, data){

        })
        .bind('fileuploadprogress', function (e, data) {
            var progress = parseInt(data.loaded / data.total * 100, 10);
        });
    
    // Load existing files:
    $('#fileupload').addClass('fileupload-processing');
    $.ajax({
        // Uncomment the following to send cross-domain cookies:
        //xhrFields: {withCredentials: true},
        url: $('#fileupload').fileupload('option', 'url'),
        dataType: 'json',
        context: $('#fileupload')[0]
    }).always(function () {
        $(this).removeClass('fileupload-processing');
    }).done(function (result) {
        $(this).fileupload('option', 'done')
            .call(this, $.Event('done'), {result: result});
    });
    

});
