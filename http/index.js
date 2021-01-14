
function $(sel) {
    return document.querySelector(sel);
}

function httpGet(url, callback) {
    var xobj = new XMLHttpRequest();
    xobj.open('GET', url);
    xobj.onreadystatechange = function () {
        if (xobj.readyState == 4 && xobj.status == '200') {
            callback(xobj.responseText);
        }
    };
    xobj.send(null);
}

httpGet('/api/v1/settings', function (res) {
    var settings = JSON.parse(res);
    Object.keys(settings).forEach(function (key) {
        if (!$('#' + key)) return;
        $('#' + key).value = settings[key];
    });
});

var getParams = window.location.search.slice(1)
    .split('&')
    .reduce(function _reduce(/*Object*/ a, /*String*/ b) {
        b = b.split('=');
        a[b[0]] = decodeURIComponent(b[1]);
        return a;
    }, {});

if (getParams['success'] == 'true') {
    $('#message').style.color = 'green';
    $('#message').innerText = 'Speichern erfolgreich';
}