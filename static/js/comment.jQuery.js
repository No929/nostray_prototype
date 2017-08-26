$('#submit').on('click',function () {
    var content = $('#comment_content').val()
    var post = $('#thispost').val()
    var csrf = $('#csrf').val()
    if (content == '') {
        alert('内容不能为空！')
        return
    }
    $.ajax({
        cache:false,
        type:'POST',
        url:'/community/comment/',
        data:{'content':content, 'post':post},
        async:true,
        beforeSend:function (xhr, settings) {
            xhr.setRequestHeader('X-CSRFToken', csrf)
        },
        success:function (data) {
            if (data.status == 'fail'){
                if (data.msg == 'NO_LOGING')
                    window.location.href = '/login/'
                else
                    alert(data.msg)
            } else if (data.status == 'success')
                window.location.reload()
        }
    })
})