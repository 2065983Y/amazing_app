$('#likes').click(function(){
    var mazename;
    mazename = $(this).attr("data-mazename");
    $.get('/mazeapp/like_maze/', {maze_name: mazename}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});