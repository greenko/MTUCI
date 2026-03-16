var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++){
    
    /*
    foldBtns[i].addEventListener("click", function(event) {
        console.log("you clicked ", event.target);
    });
    */

    foldBtns[i].addEventListener("click", function(e) {
        var postBlock = e.target.parentElement.parentElement.parentElement;

        if (postBlock.className.indexOf('folded') !== -1) {
            // свёрнут — разворачиваем
            postBlock.className = 'one-post';
            e.target.innerHTML = 'Свернуть';
        } else {
            // развёрнут — сворачиваем
            postBlock.className = 'one-post folded';
            e.target.innerHTML = 'Развернуть';
        }
    });
}
