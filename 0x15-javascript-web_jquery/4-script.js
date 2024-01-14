// when a user clicks on the tag DIV#toggle_header
// JS script will toggles the class of the <header> element

$('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green');
});
