const content = 'content.html';
let lastUpdate = null;

function updateContent() {
    fetch(location + content)
        .then(res => {
            if (checkIsNewDate(res.headers.get('Last-Modified'))) {
                setContent();
            }
        });
}

function checkIsNewDate(d) {
    let testDate = Date.parse(d)
    if (lastUpdate == null) {
        lastUpdate = testDate;
        return true
    } else if (testDate > lastUpdate) {
        lastUpdate = testDate;
        return true;
    }
    return false;
}

function setContent() {
    document.getElementById("content")
        .setAttribute("data", "./content.html")
}

function init() {
    setInterval(() => {
        updateContent();
    }, 5000);
}

init();