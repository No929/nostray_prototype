//jQuery praise animation
	$(function(){
		$("#praise").click(function(){
			var praise_img = $("#praise-img")
			var text_box = $("#add-num")
			var praise_txt = $("#praise-txt")
			var num=parseInt(praise_txt.text())
			if(praise_img.attr("src") == ("/static/img/liked.png")){
				$(this).html("<img src='/static/img/like.png' id='praise-img' class='animation' />" +
					"<input type='hidden' name='like_count' value=-1>")
				praise_txt.removeClass("hover")
				text_box.show().html("<em class='add-animation'>-1</em>")
				$(".add-animation").removeClass("hover")
				num -=1
				praise_txt.text(num)
			}else{
				$(this).html("<img src='/static/img/liked.png' id='praise-img' class='animation' />" +
					"<input type='hidden' name='like_count' value=1>")
				praise_txt.addClass("hover")
				text_box.show().html("<em class='add-animation'>+1</em>")
				$(".add-animation").addClass("hover")
				num +=1
				praise_txt.text(num)
			}
		})
	})