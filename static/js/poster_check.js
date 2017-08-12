function titleChange(obj) {
    if (obj.length>20 || obj.length<1)
        document.getElementById('title_error').innerHTML =
            '<span>标题长度不规范(1-20)</span>';
    else {
        document.getElementById('title_error').innerHTML =
            '<span></span>';
    }
}

function contentChange(obj) {
    if (obj.length>2000 || obj.length<1)
        document.getElementById('content_error').innerHTML =
            '<span>内容长度不规范(1-2000)</span>';
    else {
        document.getElementById('content_error').innerHTML =
            '<span></span>';
    }
}

function imgChange(obj) {
    if (obj.length != 0) {
        document.getElementById("img_error").innerHTML =
            "<span></span>";
        var path = document.getElementById("img_input").value;
        document.getElementById("img_root").innerHTML = path;
    }
}

function clearImg() {
    document.getElementById("img_input").value = '';
    document.getElementById("img_root").innerHTML = '无';
}