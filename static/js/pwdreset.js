var flag1 = false, flag2 = false;
function chang1(obj) {
	var obValue = obj.value;
	
	if (obValue.length > 16 || obValue.length < 6) {
		var style = document.getElementById("txt1");
		style.style.color='red';
		document.getElementById("txt1").value = "·长度要求6~16位";	
		flag1=false;	
	} else {
		var style = document.getElementById("txt1");
		style.style.color='green';
		document.getElementById("txt1").value = "·√";
		flag1=true;
	}
}
function chang2(obj) {
	var Value2 = obj.value;
	var Value1 = document.getElementById("pw1").value;
	
	if(Value2.length > 16 || Value2.length < 6){
		var style = document.getElementById("txt2");
		style.style.color='red';
		document.getElementById("txt2").value = "·长度要求6~16位";	
		flag2=false;
	}else if (Value1 != Value2) {
		var style = document.getElementById("txt2");
		style.style.color='red';
		document.getElementById("txt2").value = "·密码和确认密码不一致！";
		flag2=false;
	} else {
		style.style.color='green';
		document.getElementById("txt2").value = "·√";
		flag2=true;
	}
}
function sub() {
	//判断
		if(flag1&&flag2){
			document.pwdreset.submit();
		}
		else{
			alert("请认真填写密码！");
			document.pwdreset.pw1.value="";
			document.pwdreset.pw2.value="";
			document.getElementById("txt1").value = "";
			document.getElementById("txt2").value = "";
		}
}