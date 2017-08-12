 $(document).ready(function () {
        $("#submitBtn").click(function () {
            $.ajax({
                type:"POST",
                url:"/community/poster/",
                dataType:"json",
                data:{
                    title:$("#title").val(),
                    content:$("#content").val(),
                    image:$("#img_input").val(),
                },
                success:function(data){
                    if (data.success){
                        $("#img_error").html(data.msg)
                    } else {
                        $("#img_error").html(data.msg)
                    }
                },
                error:function (jqXHR) {
                    alert("发生错误："+jqXHR.status)
                }
            })
        })
    })