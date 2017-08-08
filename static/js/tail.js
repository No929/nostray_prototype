$(window).scroll(function(){
　　var scrollTop = $(this).scrollTop()
　　var scrollHeight = $(document).height()
　　var windowHeight = $(this).height()
　　if(scrollTop + windowHeight == scrollHeight){
　　　　$("#tail").html("<div class='inner_tail'>" +
        "<div class='tail_links'>" +
        "<a class='links' href=''>法律法规</a><a class='links' href=''>商业合作</a>" +
        "<a class='links' href=''>联系我们</a><a class='links' href=''>关于我们</a>" +
        "</div>" +
        "<span class='copyright'>Copyright © 2017 nostray 鲁ICP备17014163号</span>" +
        "</div>")
　　} else {
      $("#tail").html("")
  }
})