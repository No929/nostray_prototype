/**
 * 
 */
window.onload=function(){
	var oBtn=document.getElementById("btn_login");
	var oBack = document.getElementById('back_top');
	var oRegist = document.getElementById('btn_regist');
	
//鼠标点击注册
	oRegist.onclick = function(){
		location = 'regist.html';
	}
	
//---------------------------------------返回顶部
	//获取页面可视区的高度
	var clienHeight = document.documentElement.clientHeight;
	var timer = null;
	var isTop = true;
	
	//滚动条滚动时触发
	window.onscroll = function(){
		var osTop = document.documentElement.scrollTop || document.body.scrollTop;
		if(osTop >= clienHeight){
			oBack.style.display = 'block';
		}else{
			oBack.style.display = 'none';
		}
		
		if(!isTop){
			clearInterval(timer);
		}
		isTop = false;
	}
	
//当鼠标点击回到顶部-------------------------------------------------------------------------------------
	oBack.onclick = function(){
		//设置计时器
		timer = setInterval(function(){
			//获取滚动条距离顶部的高度
			var osTop = document.documentElement.scrollTop || document.body.scrollTop;
			var ispeed = Math.floor(-osTop / 6);
			document.documentElement.scrollTop = document.body.scrollTop = osTop + ispeed;
			
			isTop = true;
			//清除计时器
			if(osTop == 0){
				clearInterval(timer);
			}
		},25)
	}
	
	

//鼠标点击时的事件----------------------------------------------------------------------------------
	oBtn.onclick=function(){
		//获取页面的高度和宽度
		var sHeight=document.documentElement.scrollHeight;
		var sWidth=document.documentElement.scrollWidth;
		//获取可视区域
		var wHeight=document.documentElement.clientHeight;
		//alert(wHeight);
		var oMask=document.createElement("div");
			oMask.id="mask";
			oMask.style.height=sHeight+"px";
			oMask.style.width=sWidth+"px";
			//插入节点
			document.body.appendChild(oMask);
		
		var oLogin=document.createElement("div");
			oLogin.id="login";
			//把div撑起来，获取oLogin的宽和高
			oLogin.innerHTML=
			"<div id='loginCon'>\
				<div id='close'>×</div>\
			    <form action='#' method='get' class='form'>\
			   	  <table height='240'>\
			        		<tr>\
			               	  <td height='95'>\
			                    	<img src='./img/logo.png'/>\
			                  </td>\
			                </tr>\
			                <tr>\
			               	  <td height='33'>\
			                   	<input type='text' name='username' id='username' required='required' placeholder='用户名'/>\
			                  </td>\
			          </tr> \
			                <tr>\
			               	  <td height='33'>\
			                    	<input type='password' name='password' id='password' required='required' placeholder='密码' />\
			                  </td>\
			                </tr> \
			                <tr>\
			                	<td height='36'>\
			                    	<input type='submit' name='_login_btn_login' id='_login_btn_login' value='登录' />\
			                    </td>\
			                </tr> \
			                <tr>\
			                	<td>\
			                  	  <input type='button' name='_login_btn_login' id='_login_btn_regist' value='注册' />\
			                    </td>\
			                </tr> \
			        </table>\
			  </form>\
			</div>";
			//插入节点
			document.body.appendChild(oLogin);	
		//获取元素的高度和宽度(写在插入节点之后，获取已有的)
		var dHeight=oLogin.offsetHeight;
		var dWidth=oLogin.offsetWidth;
			//给login的left和top赋值
			oLogin.style.left=(sWidth-dWidth)/2+"px";
			oLogin.style.top=(wHeight-dHeight)/2+"px";
		
		var oClose=document.getElementById("close");
			//点击关闭时，删除遮罩层和登录框
			oMask.onclick=oClose.onclick=function(){
				//删除遮罩层
				document.body.removeChild(oMask);
				//删除登录框
				document.body.removeChild(oLogin);
			}
	}	
}