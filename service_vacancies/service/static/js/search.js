document.querySelector(".search").addEventListener("input", function(){
    let val = this.value.trim().toLowerCase();
    let itemsText = document.querySelectorAll(".element");
    if(val != ''){
        itemsText.forEach(elem => {
            if(elem.textContent.toLowerCase().search(val) == -1){
                elem.classList.add('hide');
            }
            else{
                elem.classList.remove('hide');
            }
        })
    }
    else{
        itemsText.forEach(elem => {
            elem.classList.remove('hide');
        });
    }
});