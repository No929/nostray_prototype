var flag1 = false, flag2 = false;

function CheckUsername(obj){

	if(obj.length<2 || obj.length>16){
		document.getElementById("name_feedback").
			innerHTML = "<font color=red>用户名长度为2-16位</font>";
		flag1 = false;
	}
	else{
		document.getElementById("name_feedback").
			innerHTML = "<font color=green>可以使用</font>";
		flag1 = true;
	}

function ChackPwd(obj){

	if(obj.length<6 || obj.length>16){
		document.getElementById("pwd_feedback").innerHTML = "密码长度为6-16位";
		document.getElementById("pwd_feedback").style.color = "red";
		flag2 = false;
	}
	else{
		document.getElementById("pwd_feedback").innerHTML = "";
		flag2 = true;
	}
}
function ClearData(){
	document.form.username.value="";
}