function toggle(tag) {
    var x = document.getElementsByName(tag)[0];
    var a = x.parentNode
    if (a.style.display == 'block') {
        a.style.display = 'none'
    } else {
        a.style.display = 'block'
    }
}


function init() {
    //this function will add show hide functionality to paired list items,
    //as long as the answer is a list item straight after the question list item.
    //You can also have as many separate lists as you want.
    //all lists must be contained within a div with id QA

    var obj = document.getElementById('QA');
    var elements = obj.getElementsByTagName('li');
    var index = 1
    //add javascript to question elements
    //you could also add styling to question elements here
    for (var i = 0; i < elements.length; i += 2) {
        var element = elements[i];
        element.innerHTML = "<a href='javascript:toggle(" + index + ")'>" + element.innerHTML + "</a>"
        index = index + 1
    }
    //add bookmark to answer elements and add styling
    var index = 1
    for (var i = 1; i < elements.length; i += 2) {
        var element = elements[i];
        element.innerHTML = "<a name='" + index + "' id='" + index + "'></a>" + element.innerHTML
        index = index + 1
        element.style.padding = '0px 0px 10px 20px' //add indent to answer
        element.style.listStyleType = 'none' //remove bullet
        element.style.display = 'none' //hide answer element
    }
}


window.onload = init;