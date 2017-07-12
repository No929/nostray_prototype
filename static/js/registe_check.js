var flag1 = false, flag2 = false, flag3 = false;


function CheckUsername(obj){
	if(obj.length<2 || obj.length>16){
		document.getElementById('name_feedback').innerHTML = "<font color='red'>用户名长度为2-16位</font>";
		flag1 = false;
	}
	else{
		document.getElementById('name_feedback').innerHTML = "<font color='green'>可以使用</font>";
		flag1 = true;
	}
}

function CheckPwd1(obj){	
	if(obj.length<6 || obj.length>16){
		document.getElementById("pwd_feedback1").innerHTML = "<font color='red'>密码长度为6-16位</font>";
		flag2 = false;
	}
	else{
		document.getElementById("pwd_feedback1").innerHTML = "<font color='green'>可以使用</font>";
		flag2 = true;
	}
}

function CheckPwd2(obj){
	var pwd1 = document.getElementById("password1").value;
	if(obj!=pwd1){
		document.getElementById("pwd_feedback2").innerHTML = "<font color='red'>两次输入密码不同</font>";
		flag3 = false;
	}
	else if(flag2==false){
		document.getElementById("pwd_feedback2").innerHTML = "<font color='red'>请重新输入密码</font>";
		flag3 = false;
	}
	else{
		document.getElementById("pwd_feedback2").innerHTML = "<font color='green'>可以使用</font>"
	}
}

function Submit(){
	if(flag1==true || flag2==true || flag3==true)
		document.form.submit();
}
