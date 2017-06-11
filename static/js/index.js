// JavaScript Document
window.onload= function(){
		var container = document.getElementById('container');
		var list = document.getElementById('list');
		var buttons = document.getElementById('buttons').getElementsByTagName('span');
		var prev = document.getElementById('prev');
		var next = document.getElementById('next');
		var index=1;
		var animated=false;
		var timer;//定时器
		
		play();
		function showButton(){
			for(var i=0;i<buttons.length;i++){
				if(buttons[i].className=='on'){
					buttons[i].className='';
					break;
				}
			}
			buttons[index-1].className='on';
		}
		
		function animate(offset){/*偏移函数*/
			animated = true;
			var newLeft=parseInt(list.style.left)+offset;
			var time = 300;//位移总时间
			var interval = 5;//位移间隔时间
			var speed = offset /(time/interval) ;//每次位移量
			
			function go(){
				if((speed < 0 && parseInt(list.style.left) > newLeft)||(speed > 0 && parseInt(list.style.left) < newLeft)){
					list.style.left = parseInt(list.style.left) + speed +'px';
					setTimeout(go,interval);
				}
				else{
					animated = false;
					list.style.left= newLeft +'px';
					if(newLeft>-1366){
						list.style.left= -5464 +'px';
					}
					if(newLeft<-5464){
						list.style.left= -1366 +'px';
					}
				}
				
			}
			
			go();
			
		}
		function play1(){
			timer=setInterval(function (){prev.onclick();},1);
			clearInterval(timer);
		}
		//自动播放
		function play(){
			timer=setInterval(function (){next.onclick();},3000);
		}
		//停止播放
		function stop(){
			clearInterval(timer);
		}
		
		next.onclick=function(){/*右按钮*/
			if(!animated){
				if(index==4){
					index=1;
				}
				else{
					index+=1;
				}
				showButton();
				//if(!animated){
					animate(-1366);
				//}
			}
			
		}
		prev.onclick=function(){/*左按钮*/
			if(!animated){
				if(index==1){
					index=4;
				}
				else{
					index-=1;
				}
				showButton();
				//if(!animated){
					animate(1366);
				//}
			}
		}
		for(var i=0; i<buttons.length;i++){/*遍历按钮*/
			buttons[i].onclick=function(){
				if(!animated){
					if(this.className=='on'){
						return;
					}
				
					var myindex=parseInt(this.getAttribute('index'));
					var offset=-1366*(myindex-index);
					
					
					//if(!animated){
						animate(offset);
					//}
					index=myindex;
					
					showButton();
				}
				
				
				
			}
		}
		container.onmouseover = stop;
		container.onmouseout = play;
}