$(function(){
	$(".ul_li").children(".ul_li_ul").hide();
	$(".ul_li").mouseover(function(){
		 $(this).children(".ul_li_ul").show();
		 })
	 $(".ul_li").children(".ul_li_ul").mouseout(function(){
		 $(this).hide();
		 })
     /*$('#a0').mousedown(function() {
		 $(".ul_li").children(".ul_li_ul").hide();
	 })
	 $('#a1').mousedown(function() {
        var txt1 = $('.ul_li').children('#a0').html();
        var txt = $('#li1').children('#a1').html();
        $('#li1').children('#a1').html(txt1);
        $('.ul_li').children('#a0').html(txt);
		$(".ul_li").children(".ul_li_ul").hide();
    });*/
})