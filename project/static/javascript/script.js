// // Header Scroll 
// let nav = document.querySelector(".navbar");
// window.onscroll = function() {
//     if(document.documentElement.scrollTop > 50){
//         nav.classList.add("header-scrolled"); 
//     }else{
//         nav.classList.remove("header-scrolled");
//     }
// }

// // nav hide  
// let navBar = document.querySelectorAll(".nav-link");
// let navCollapse = document.querySelector(".navbar-collapse.collapse");
// navBar.forEach(function(a){
//     a.addEventListener("click", function(){
//         navCollapse.classList.remove("show");
//     })
// })

// // ----------------------------------------------
// // landing page start


// // landing page end 


// // ----------------------------------------------

// // about section start 


// // about section end  
// // ----------------------------------------------

// // donation process section start 
// const stepButtons = document.querySelectorAll('.step-button');
// const progress = document.querySelector('#progress');

// Array.from(stepButtons).forEach((button,index) => {
//     button.addEventListener('click', () => {
//         progress.setAttribute('value', index * 100 /(stepButtons.length - 1) );//there are 3 buttons. 2 spaces.

//         stepButtons.forEach((item, secindex)=>{
//             if(index > secindex){
//                 item.classList.add('done');
//             }
//             if(index < secindex){
//                 item.classList.remove('done');
//             }
//         })
//     })
// })

// const stepButton1 = document.getElementsByClassName('step-button')[0];
// const stepButton2 = document.getElementsByClassName('step-button')[1];
// const stepButton3 = document.getElementsByClassName('step-button')[2];


// let card1 = document.getElementById("collapseOne");
// let card2 = document.getElementById("collapseTwo");
// let card3 = document.getElementById("collapseThree");

// card2.parentNode.style.display= "none"
// card3.parentNode.style.display= "none"

// stepButton1.onclick = function (){
//    stepButton1.classList.remove("collapsed")
//    stepButton2.classList.add("collapsed") 
//    stepButton3.classList.add("collapsed") 

//    stepButton1.setAttribute("aria-expanded", "true")
//    stepButton2.setAttribute("aria-expanded", "false")
//    stepButton3.setAttribute("aria-expanded", "false")

//    card1.classList.add("show")
//    card2.classList.remove("show") 
//    card3.classList.remove("show") 

//     card1.parentNode.style.display = "block"
//     card2.parentNode.style.display = "none"
//     card3.parentNode.style.display = "none"

// }
// stepButton2.onclick = function (){
//     stepButton2.classList.remove("collapsed")
//     stepButton1.classList.add("collapsed") 
//     stepButton3.classList.add("collapsed") 

//     stepButton2.setAttribute("aria-expanded", "true")
//     stepButton1.setAttribute("aria-expanded", "false")
//     stepButton3.setAttribute("aria-expanded", "false")

//     card2.classList.add("show")
//     card1.classList.remove("show") 
//     card3.classList.remove("show") 

//     card2.parentNode.style.display = "block"
//     card1.parentNode.style.display = "none"
//     card3.parentNode.style.display = "none"
 
//  }
//  stepButton3.onclick = function (){
//     stepButton3.classList.remove("collapsed")
//     stepButton2.classList.add("collapsed") 
//     stepButton1.classList.add("collapsed") 


//     stepButton3.setAttribute("aria-expanded", "true")
//     stepButton2.setAttribute("aria-expanded", "false")
//     stepButton1.setAttribute("aria-expanded", "false")
 
//     card3.classList.add("show")
//     card1.classList.remove("show") 
//     card2.classList.remove("show") 

//     card3.parentNode.style.display = "block"
//     card1.parentNode.style.display = "none"
//     card2.parentNode.style.display = "none"
//  }

// Header Scroll 
let nav = document.querySelector(".navbar");
window.onscroll = function() {
    if(document.documentElement.scrollTop > 50){
        nav.classList.add("header-scrolled"); 
    }else{
        nav.classList.remove("header-scrolled");
    }
}

// nav hide  
let navBar = document.querySelectorAll(".nav-link");
let navCollapse = document.querySelector(".navbar-collapse.collapse");
navBar.forEach(function(a){
    a.addEventListener("click", function(){
        navCollapse.classList.remove("show");
    })
})

// ----------------------------------------------
// landing page start


// landing page end 


// ----------------------------------------------

// about section start 


// about section end  
// ----------------------------------------------

// donation process section start 
const stepButtons = document.querySelectorAll('.step-button');
const progress = document.querySelector('#progress');

Array.from(stepButtons).forEach((button,index) => {
    button.addEventListener('click', () => {
        progress.setAttribute('value', index * 100 /(stepButtons.length - 1) );//there are 3 buttons. 2 spaces.

        stepButtons.forEach((item, secindex)=>{
            if(index > secindex){
                item.classList.add('done');
            }
            if(index < secindex){
                item.classList.remove('done');
            }
        })
    })
})

const stepButton1 = document.getElementsByClassName('step-button')[0];
const stepButton2 = document.getElementsByClassName('step-button')[1];
const stepButton3 = document.getElementsByClassName('step-button')[2];


let card1 = document.getElementById("collapseOne");
let card2 = document.getElementById("collapseTwo");
let card3 = document.getElementById("collapseThree");

card2.parentNode.style.display= "none"
card3.parentNode.style.display= "none"

stepButton1.onclick = function (){
   stepButton1.classList.remove("collapsed")
   stepButton2.classList.add("collapsed") 
   stepButton3.classList.add("collapsed") 

   stepButton1.setAttribute("aria-expanded", "true")
   stepButton2.setAttribute("aria-expanded", "false")
   stepButton3.setAttribute("aria-expanded", "false")

   card1.classList.add("show")
   card2.classList.remove("show") 
   card3.classList.remove("show") 

    card1.parentNode.style.display = "block"
    card2.parentNode.style.display = "none"
    card3.parentNode.style.display = "none"

}
stepButton2.onclick = function (){
    stepButton2.classList.remove("collapsed")
    stepButton1.classList.add("collapsed") 
    stepButton3.classList.add("collapsed") 

    stepButton2.setAttribute("aria-expanded", "true")
    stepButton1.setAttribute("aria-expanded", "false")
    stepButton3.setAttribute("aria-expanded", "false")

    card2.classList.add("show")
    card1.classList.remove("show") 
    card3.classList.remove("show") 

    card2.parentNode.style.display = "block"
    card1.parentNode.style.display = "none"
    card3.parentNode.style.display = "none"
 
 }
 stepButton3.onclick = function (){
    stepButton3.classList.remove("collapsed")
    stepButton2.classList.add("collapsed") 
    stepButton1.classList.add("collapsed") 


    stepButton3.setAttribute("aria-expanded", "true")
    stepButton2.setAttribute("aria-expanded", "false")
    stepButton1.setAttribute("aria-expanded", "false")
 
    card3.classList.add("show")
    card1.classList.remove("show") 
    card2.classList.remove("show") 

    card3.parentNode.style.display = "block"
    card1.parentNode.style.display = "none"
    card2.parentNode.style.display = "none"
 }


// donation process section end 

// donation section start 






// donation section end 


// ----------------------------------------------

// contact section start 

// contact section end 
