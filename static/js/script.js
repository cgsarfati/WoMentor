"use strict";

$("#mentorBox").on('click', function(){
    // $(this).prop('hidden', 'hidden');
    console.log("hi");
    $(this.parentElement.parentElement).prop('hidden', 'hidden');
    console.log("hello");
    this.parentElement.parentElement.parentElement.children[2].removeAttribute("hidden");
});


// $(".infoBtn").on("click", function(evt){
//     console.log("hide me!");
//     this.parentElement.children[3].removeAttribute("hidden");
//     this.parentElement.children[2].removeAttribute("hidden");
//     this.parentElement.children[4].removeAttribute("hidden");
//     $(this).prop('hidden', 'hidden');
// });