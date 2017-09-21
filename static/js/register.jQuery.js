$('#image_url').on('click', function () {
    var csrf = $('#csrf').val()
    $.ajax({
        cache:false,
        type:'POST',
        url:'/registe/',
        data:{'refresh':'refresh'},
        async:true,
        beforeSend:function (xhr, settings) {
            xhr.setRequestHeader('X-CSRFToken', csrf)
        },
        success: function (data) {
            $('#hashkey').val(data.hashkey)
            $('#image_url').attr('src', data.image_url)
        }
    })
})

//selection animation
var btn = document.querySelector("button")
var dropdown = document.querySelector(".dropdown-options")
var optionLinks = document.querySelectorAll(".option a")
console.log(optionLinks)

btn.addEventListener("click", function(e) {
   e.preventDefault()
   console.log("btn")
   dropdown.classList.toggle("open")
});

var clickFn = function(e) {
   e.preventDefault()
   dropdown.classList.remove("open")
   btn.innerHTML = this.text
   $('#kind').val(btn.innerHTML)
   var activeLink = document.querySelector(".option .active")

   if (activeLink) {
      activeLink.classList.remove("active")
   }
   this.classList.add("active")
}
for (var i = 0; i < optionLinks.length; i++) {
   optionLinks[i].addEventListener("mousedown", clickFn, false)
}

//form check
var flag1 = false, flag2 = false, flag3 = false, flag4 = false
function usernameCheck() {
    var username = $('#username')
    if (username.val().length > 15 || username.val().length < 2) {
        $('#usrfeedback').html('长度不合法')
    } else {
        $('#usrfeedback').html("<img src='/static/img/checked.png'>")
        flag1 = true
    }

}
function pwd1Check() {
    var pwd1 = $('#pwd1')
    var pwd2 = $('#pwd2')
    if (pwd1.val().length < 6 || pwd1.length > 16) {
        $('#pwd1feeback').html('不合法密码长度( 6-16位 )')
        pwd2.attr('disabled', true)
    } else {
        $('#pwd1feeback').html("<img src='/static/img/checked.png'>")
        flag2 = true
        pwd2.attr('disabled', false)
    }
}
function pwd2Check() {
    var pwd1 = $('#pwd1')
    var pwd2 = $('#pwd2')
    if (pwd2.val() != pwd1.val()) {
        $('#pwd2feeback').html('两次输入密码不一致')
    } else {
        $('#pwd2feeback').html("<img src='/static/img/checked.png'>")
        flag3 = true
    }
}
function submit() {
    if (btn.innerHTML == '注册类型'){
        alert('请选择账户类型')
    } else {
        flag4 = true
    }
    if (flag1 == flag2 == flag3 == flag4 == true)
        $('#form').submit()
}
function captcha(obj, csrf) {
    $.ajax({
        cache:false,
        type:'POST',
        url:'/registe/',
        data:{'captcha':obj},
        async:true,
        beforeSend:function (xhr, settings) {
            xhr.setRequestHeader('X-CSRFToken', csrf)
        },
        sucess: function (data) {

        }
    })
}
