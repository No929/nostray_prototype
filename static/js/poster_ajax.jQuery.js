function poster(elem, csrf, title, content, img, type) {
    $.ajax({
        type:"POST",
        url:"/community/poster",
        data:{'title':title, 'content':content, 'img':img, 'post_cate':type},
        beforeSend:function (xhr, settings) {
            xhr.setRequestHeader('X-CSRFToken', csrf)
        },
        success: function (data) {
            if (data.status == 'fail'){
                if (data.msg == 'NO_LOGIN')
                    window.location.href = '/login/'
                else
                    elem.html(data.msg)
            } else if (data.status == 'success'){
                title = ''
                content = ''
                img = ''
                type = ''
            }
        }
        })
}