$(document).ready(function() { // this is the way to begin with JQuery

    $('#birth-date, #visitdate').datepicker({
        dateFormat: "yy-mm-dd"
    });

    $('#birth-date').on('change', function() {
        var dob = new Date($('#birth-date').val());
        var today = new Date();
        var age = Math.floor((today - dob) / (365.25 * 24 * 60 * 60 * 1000)); // $('#age').val(age); // });
        $('#age').val(age);
    });

})

$(document).ready(function() {
    
    $('#left-savepat-div, #right-savepat-div').animate({
        padding: "10px",
        margin: "20px",
        width: "500px",
        height: "500px"
    }, 500);

    $("#edit-visits-div, #savevis-div").animate({
        padding: "10px",
        margin: "20px",
        width: "100%",
        height: "100%"
    }, 500);

    $("#left, #right").animate({
        padding: "10px",
        margin: "20px",
        width: "500px",
        height: "600px"
    }, 500);

    $("#left-savevis-div, #right-savevis-div, #left-saverevis-div, #right-saverevis-div").animate({
        padding: "10px",
        margin: "20px",
        width: "500px",
        height: "600px"
    }, 500);

})

// for Edit Form
$(document).ready(function() {

    $("#edit-pat-div").css({
        padding: "10px",
        margin: "20px",
        width: "100%",
        height: "100%"
    });

    $("#edit-pat-table-div").css({
        padding: "10px",
        margin: "20px",
        width: "700px",
        height: "700px"
    });

    $("#left-editpat-div").css({
        padding: "10px",
        margin: "20px",
        width: "400px",
        height: "700px"
    });
})

// for drug
$(document).ready(function() {
    // var arabicPattern = /[\u0600-\u06FF]/;

    // $('#plan').bind('input propertychange', function(ev) {
    //     var text = ev.target.value;
    //     if (arabicPattern.test(text)) {
    //         // arabic;
    //         $('#plan').css('direction', 'rtl')
    //     }
    // });

    // $(document).on('focus', '#plan', function() {
    //     this.attr('lang', 'arabisk')
    // });
    // $(document).on('outfocus', '#plan', function() {
    //     this.attr('lang', 'eng')
    // });

    $("#save-drug-div, #edit-drug-div").css({
        padding: "10px",
        margin: "20px",
        width: "100%",
        height: "100%"
    });

    $("#left-save-drug-div, #left-edit-drug-div").css({
        padding: "10px",
        margin: "20px",
        width: "400px",
        height: "500px"
    });

    $("#drug-table-div").css({
        padding: "10px",
        margin: "20px",
        width: "700px",
        height: "600px"
    });
})


// $('#birth-date').on('change', function() {
//     var age = getAge(new Date($("#birth-date").value()));
//     $("#age").value(age)
// });
// function getAge(dateString) {
//     var today = new Date();
//     var birthDate = new Date(dateString);
//     var age = today.getFullYear() - birthDate.getFullYear();
//     var m = today.getMonth() - birthDate.getMonth();
//     if ((m < 0) || (m === 0) && (today.getDate()) < (birthDate.getDate())) {
//         age--;
//     }
//     return age;
// };



// color for button
// $('#edit-patient, #new-visit, #vis-form-btn').css("color", "darkblue");
// $('#vis-form-btn').css('background', 'white');

// $('#birth-date').css('background', 'pink');


//
// $('#birth-date').bind('blur', function() {
//     // alert('date')
//     var dob = new Date($('#birth-date').value());
//     var today = new Date();
//     var age = Math.floor((today - dob) / (365.25 * 24 * 60 * 60 * 1000));
//     $('#age').value(age);
// });


// 
// $('[name=quantity], [name=price]').on('input', function() {
//     $('[name=total]').val(parseInt($('[name=quantity]').val()) * parseInt($('[name=price]').val()));
// });

// Occurs on button click 
// $('#btn-edit-items').on('click', function() {
//     $('[name=total]').val(parseInt($('[name=quantity]').val()) * parseInt($('[name=price]').val()));
// });

// Occurs on button(submit) on click  
// $('#btn-add-bill').on('click', function() {
//     $('[name=remain]').val(parseInt($('[name=sumtotal]').val()) - parseInt($('[name=paid]').val()));
//     if (parseInt($('[name=remain]').val()) == 0) {
//         $('#paidDone option:contains(false)').attr('selected', true); // the way to assign a value to a dropdown(choice field)
//         $('#returns').attr('checked', false); // this is the way to assign a true or false to a checkbox
//     }
// });

// Occurs on button(update) click  
// $('#btn-editbills').click(function() {
//     // alert('clicked');
//     $('[name=remain]').val(parseInt($('[name=sumtotal]').val()) - parseInt($('[name=paid]').val()));
//     if (parseInt($('[name=paid]').val()) > 0 && parseInt($('[name=sumtotal]').val()) == parseInt($('[name=paid]').val()) && parseInt($('[name=remain]').val()) == 0) {
//         $('#paidDone option:contains(true)').attr('selected', true);
//         // alert('it is finished');
//         // $('#paidDone').val(x).change();
//         // $('#returns').attr('checked', true); // this the method to assign a true or false to a checkbox
//     } else {
//         $('#paidDone option:contains(false)').attr('selected', false);
//     }
//     if ($('[name=sumtotal]').text('')) {
//         // alert('it is empty');
//         parseInt($('[name=sumtotal]').val(0));
//         // ('[name=sumtotal]').text('0');
//     }
// });

// Occurs when the text changed
// $('[name=sumtotal], [name=paid]').on('input', function() {
//     // alert("hi done");
//     $('[name=remain]').val(parseInt($('[name=sumtotal]').val()) - parseInt($('[name=paid]').val()));
// });
// $('[name=sumtotal], [name=paid]').on('input', function() {
//     if (parseInt($('[name=remain]').val()) == 0) {
//         // $('#paidDone').val('');
//         // $('#paidDone').val('true');
//         // $('#paidDone').val(true);
//         $('#returns').val(true);
//     }
// });

// This snippet occurs when the form load when we enter the page or refresh it, this is dueto callback function
// $("#f-editbills").animate({
//     padding: "10px",
//     margin: "20px",
//     width: "1000px",
//     height: "1000px"
// }, 500);

// $("#btn-add-bill").on('click', function() {
//     $('[name=sumtotal], [name=paid], [name=remain]').val(0)
// });
// $('#pro_editform').css("background-color", "lightblue")
// $("#edit-items, #f-newitems, #pro_editform").animate({
//     padding: "5px",
//     margin: "10px",
//     width: "1100px",
//     height: "1625px"
// }, 500);

// $(function() {
//     $('#birth-date').datepicker({
//         dateFormat: "yy-mm-dd"
//     });
// });



// $("#login").animate({
//     padding: "10px",
//     margin: "20px",
//     width: "800px",
//     height: "800px"
// }, 500);

// $("#expandform").animate({
//     padding: "3px",
//     margin: "3px",
//     width: "1000px",
//     height: "1200px"
// });

// $("#form2").animate({
//     padding: "3px",
//     margin: "3px",
//     width: "900px",
//     height: "800px"
// }, 500);

// // $('#save').css('color', '');
// $("#save").animate({
//     padding: "3px",
//     margin: "3px",
//     width: "500px",
//     height: "100px"
// }, 500);

// $('#save').hideToggle()

// $("#image").animate({
// // padding: "3px",
// // margin: "3px",
// width: "1500px",
// height: "1000px"
// }, 200);


// $('#total').val(0);

// $('#datepicker1, #enddate').datepicker({
//     dateFormat: "yy-mm-dd"
// });

// $(function() {
//     $("#edit-items").animate({
//         padding: "10px",
//         margin: "20px",
//         width: "800px",
//         height: "800px"
//     }, 500);
// });

// $("#edit-items", "#f-add-bill", "#f-editbills").animate({
//     padding: "10px",
//     margin: "20px",
//     width: "800px",
//     height: "800px"
// }, 500);

// $(function() {
//     $("#edit-items", "#f-newitems", "#f-editbills", "#f-add-bill").animate({
//         padding: "10px",
//         margin: "20px",
//         width: "800px",
//         height: "800px"
//     }, 500);
// });

// $(function() {
//     $("#f-add-bill").animate({
//         padding: "10px",
//         margin: "20px",
//         width: "800px",
//         height: "800px"
//     }, 500);
// });

// $(function() {
//     $("#f-newitems", "#f-add-bill").animate({
//         padding: "10px",
//         margin: "20px",
//         width: "800px",
//         height: "800px"
//     }, 500);
// });

// $("#d-editbill").animate({
//     padding: "10px",
//     margin: "20px",
//     width: "400px",
//     height: "400px"
// }, 500);

// $(function (){
//     $('[name=datepicker1]').datepicker("setDate", new Date(2008, 9, 03));
// });

// $('#launtype, #price, #quantity').html(document.getElementById('#launtype, #price, #quantity').innerText)
// $('[name=remain]').val(parseInt($('[name=sumtotal]').val()) - parseInt($('[name=paid]').val()));
// $('[name=sumtotal], [name=paid]').focus(function() {
//     $('[name=remain]').val(parseInt($('[name=sumtotal]').val()) - parseInt($('[name=paid]').val()));
// });
// $('[name=sumtotal], [name=paid]').find('select, input').change();
// $('#table tr').click(function() {
//     var href = $(this).find("a").attr("href");
//     if (href) {
//         window.location = href;
//     }
// });

// $("#divfooter").animate({
//     padding: '5px',
//     margin: '5px'
//         // width: "inline"
// });

// $(function () {
//     $('#datepicker1').datetimepicker({
//         minDate: moment().startOf('minute').add(180, 'm'),
//     });
// });

// setInterval(function () {
//     var pickedDate = $('#datepicker1').data('DateTimePicker').date();
//     var currentDate = moment();
//     pickedDate = pickedDate.set({
//         'hour': currentDate.get('hour') + 3,
//         'minute': currentDate.get('minute'),
//         'second': currentDate.get('second')
//     });
//     $('#datepicker1').data("DateTimePicker").date(pickedDate);
// }, 1000);

// $('#datetimepicker1').datepicker();

// $('#all').css("color", "lightgrey");
// $("#lb_select").css("color", "black");
// $("#p-signup").css("color", "blue");
// $("#record").css("color", "white");
// $("#p-signup").css("color", "blue");
// $("#record").css("color", "white");
// })