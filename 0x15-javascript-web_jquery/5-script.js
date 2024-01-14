// adds a <li> element to a list
// when a user clicks on the tag DIV#add_item:

$('#add_item').click(function () {
    $('ul').append('<li>Item</li>');
});
