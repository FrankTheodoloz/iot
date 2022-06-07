const content = './content.html';
let i = 0;
currentData = null;

function switchContent() {

    let current = $("#content" + i % 2);        //   4=0 |   5=1
    let other = $("#content" + (i + 1) % 2);    // 4+1=1 | 5+1=0

    // current.load(content, function(){
    //     $(this).contents().unwrap();
    // }).fadeIn;
    //
    // other.load(content, function(){
    //     $(this).contents().unwrap();
    // }).fadeIn;

    other.attr('data', content);
    console.log(current.attr('data'));
    console.log(other.attr('data', content));

    if (current.get('data') !== other.attr('data', content)) {
        current.fadeOut();
        other.fadeIn();

        current.zIndex = current.zIndex - 1;
        i++;
    }

    // $("#content0").load(content, function(){
    //     $(this).contents().unwrap();
    // });
}

function includeHTML() {
  var z, i, elmnt, file, xhttp;
  /* Loop through a collection of all HTML elements: */
  z = document.getElementsByTagName("*");
  for (i = 0; i < z.length; i++) {
    elmnt = z[i];
    /*search for elements with a certain atrribute:*/
    file = elmnt.getAttribute("w3-include-html");
    if (file) {
      /* Make an HTTP request using the attribute value as the file name: */
      xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
          if (this.status == 200) {elmnt.innerHTML = this.responseText;}
          if (this.status == 404) {elmnt.innerHTML = "Page not found.";}
          /* Remove the attribute, and call this function once more: */
          elmnt.removeAttribute("w3-include-html");
          includeHTML();
        }
      }
      xhttp.open("GET", file, true);
      xhttp.send();
      /* Exit the function: */
      return;
    }
  }
}

function refresh(){
    var obj = document.getElementById("content");
    obj.data = './content.html';
}

function init() {
    switchContent();
    setInterval(() => {
        switchContent();
    }, 5000);
}

console.log("data");
//setInterval(_=>{}, 5000)();
fetch("./content.html").then(res=>{
    console.log(res.headers.get('Last-Modified'));
});

init();