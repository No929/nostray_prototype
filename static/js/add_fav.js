function add_fav(current_elem, fav_id, fav_type, csrf){
    $.ajax({
        cache: false,
        type: "POST",
        url:"/community/fav/",
        data:{'fav_id':parseInt(fav_id), 'fav_type':fav_type},
        async: true,
        beforeSend:function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", csrf);
        },
        success: function(data) {
            if(data.status == 'fail'){
                if(data.msg == '未登录'){
                    window.location.href="/login/";
                }else{
                    alert(data.msg)
                }

            }else if(data.status == 'success'){
                current_elem.text(data.msg)
            }
        },
    });
}