var flag1, flag2, flag3 = false;

function titleChange(obj) {
    if (obj.length>20 || obj.length<1)
        document.getElementById('title_error').innerHTML =
            '<span>标题长度不规范(1-20)</span>';
    else {
        document.getElementById('title_error').innerHTML =
            '<span></span>';
        flag1 = true;
    }
}

function contentChange(obj) {
    if (obj.length>5 || obj.length<1)
        document.getElementById('content_error').innerHTML =
            '<span>内容长度不规范(1-2000)</span>';
    else {
        document.getElementById('content_error').innerHTML =
            '<span></span>';
        flag2 = true;
    }
}

function imgChange(obj) {
    if (obj.length != 0) {
        flag3 = true;
        document.getElementById("img_error").innerHTML =
            "<span></span>"
    }
}

function poster_submit() {
    if (flag1 == true&&flag2 == true&&flag3 == true)
        document.getElementById("posterForm").submit()

    if (flag3 == false)
        document.getElementById("img_error").innerHTML =
            "<span>未上传图片</span>";

    var title = document.getElementById("title").value
    var content = document.getElementById("content").value
    if (title == '' || content == '')
        alert('请填检查内容完整性');
}