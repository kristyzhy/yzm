function resp() {
    let xhr = new XMLHttpRequest();
    xhr.open('GET','http://thinkloading.natapp1.cc/task');
    xhr.send();
    xhr.onload = function (res) {
        if (xhr.status == 200) {
            alert(res.target.responseText)
        };
}}