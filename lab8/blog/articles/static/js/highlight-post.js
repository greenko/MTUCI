/*
$(document).ready(function(){
    $('.one-post').hover(function(event){
        console.log("Навели. currentTarget:" + event.currentTarget + " Target:" + event.target);
    }, function(event){
        console.log("Вывели");
    });
});
*/

$(document).ready(function(){
    $('.one-post').hover(
        function(event){
            $(event.currentTarget).find('.one-post-shadow').animate({opacity:'0.1'}, 300);
        }, 
        function(event){
            $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'}, 300);
        }
    )
});

$(document).ready(function() {
    $('.header img').hover(
        function() {
            var $img = $(this);
            
            // Сохраняем исходные размеры при наведении
            var origWidth = $img.data('origW');
            var origHeight = $img.data('origH');
            if (!origWidth) {
                origWidth = $img.width();
                origHeight = $img.height();
                $img.data('origW', origWidth);
                $img.data('origH', origHeight);
            }
            
            // Новые размеры: ширина +20px, высота пропорционально
            var newWidth = origWidth + 20;
            var newHeight = origHeight * (newWidth / origWidth);
            
            $img.stop().animate({ width: newWidth, height: newHeight }, 200);
        },
        function() {
            // При уходе мыши возвращаем исходные размеры
            var $img = $(this);
            var origWidth = $img.data('origW');
            var origHeight = $img.data('origH');
            if (origWidth) {
                $img.stop().animate({ width: origWidth, height: origHeight }, 200);
            }
        }
    );
});