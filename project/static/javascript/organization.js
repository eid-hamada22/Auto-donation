$(document).ready(function () {
    $('#example').DataTable();
});

// -------------------
// let mybutton = document.getElementById("button-addon2");

// let mytextboxtext = document.getElementsByClassName("text-box");

// let mytbody = document.getElementsByTagName("tbody")[0];
// const toastLiveExample = document.getElementById('liveToast');




// mybutton.onclick = function (){


//       if (mytextboxtext[0].value !== "" && mytextboxtext[1].value !== "" && mytextboxtext[2].value !== ""){
//      console.log(" success");

//      let mytr = document.createElement("tr");

//      let mytd1 = document.createElement("td");
//      let mytd2 = document.createElement("td");
//      let mytd3 = document.createElement("td");
//      let myspan1 =document.createElement("span")
//      let myspan2 =document.createElement("span")
//      let myspan3 =document.createElement("span")

//      let closebutton = document.createElement("button")
//      closebutton.type= "button";
//      closebutton.classList.add("btn-close");
//      closebutton.ariaLabel = "Close";
//      closebutton.setAttribute("data-bs-toggle", "modal"); 
//      closebutton.setAttribute("data-bs-target", "#exampleModal"); 

//      myspan1.innerHTML= mytextboxtext[2].value;   
//      myspan2.innerHTML= mytextboxtext[1].value;   
//      myspan3.innerHTML= mytextboxtext[0].value;   
         
//      mytd1.classList.add("text-break");
//      mytd1.classList.add("text-break");
//      mytd1.classList.add("text-break");

     
//      mytd1.append(myspan1);
//      mytd1.prepend(closebutton);
//      mytd2.append(myspan2);
//      mytd3.append(myspan3);
    
//      mytr.append(mytd1);
//      mytr.append(mytd2);
//      mytr.append(mytd3);


//      mytbody.append(mytr);
    

//     if (mybutton ) {
//         mybutton.addEventListener('click', () => {
//           const toast = new bootstrap.Toast(toastLiveExample)
      
//           toast.show()
//         })
//       }
// }

//     }
 

 
// ------------------------------- modal area
let Changebtn = document.getElementsByClassName("modal-change2")[0];
let modal = document.getElementsByClassName("modal")[0];
let myclose_btns = document.getElementsByClassName("btn-close")


// ------------------------------- add-donation-start
let myselectitem = document.getElementsByClassName("special-donation-type")[0];
let myclothessection = document.getElementsByClassName("clothes-section")[0]
let myschoolsection = document.getElementsByClassName("school-section")[0]

let myclothes_numbers = document.getElementsByClassName("clothes-numbers-select")[0];
let myclothes_type = document.getElementsByClassName("clothes-type-select")[0];
let myform_file1 = document.getElementsByClassName("form-file-input") [0];
let mybutton_side = document.getElementById("dontation1");

let myschool_type = document.getElementsByClassName("school-items-select")[0];
let myform_file2 = document.getElementsByClassName("form-file-input")[1];
let textarea_clothes = document.getElementsByClassName("special-text-area")[0];
let textarea_schools = document.getElementsByClassName("special-text-area")[1];

let mybutton_side2 = document.getElementById("dontation2");

// textarea_clothes.addEventListener('input', () => {
// })

const toastLiveExample = document.getElementById('liveToast');

myclothessection.style.display = "none"
myschoolsection.style.display = "none"

myselectitem.onchange = function (){
    if(myselectitem.value === "clothes"){
      myclothessection.style.display ="flex";
      myschoolsection.style.display ="none";
    }
    if(myselectitem.value === "school-items"){
      myclothessection.style.display ="none";
      myschoolsection.style.display ="block";
    }
}

 mybutton_side.onclick = function(){
  if (myclothes_numbers.value == "notachoice" || myclothes_type.value == "notachoice" || myform_file1.files.length == 0 || textarea_clothes.value == ""){
     console.log("there is no sufficient info")
  }
   else{
      mybutton_side.addEventListener('click', () => {
          const toast = new bootstrap.Toast(toastLiveExample)
      
          toast.show()
        })
      }
  
}



mybutton_side2.onclick = function(){
  if (myschool_type.value == "notachoice"|| myform_file2.files.length == 0 || textarea_schools.value == ""){
     console.log("there is no sufficient info")
  
    }
   else{
    mybutton_side2.addEventListener('click', () => {
      const toast = new bootstrap.Toast(toastLiveExample)
  
      toast.show()
      })
  
}
}


// wishing list start 



// -------------- phone-search 



//  for (const phoneli of phonelis) {
//   phoneli.addEventListener('click', (event) => {
//         console.log(55555555555555555)
//   }); 
// }
done_btn.onclick = function () {
  about_content.style.display = "none"
  card_area.style.display ="block"
}


// --------------
$(function(){

  $('input[type="number"]').niceNumber();

});



const card_titles = document.getElementsByClassName("card-title");
const searchInput = document.getElementById("special-search");
let card_paernts = document.getElementsByClassName("special-card");

let mygivebuttons = document.getElementsByClassName("give-button")
let card_content = document.getElementsByClassName("card-content")[0];
// card_content.style.display=" none"

searchInput.addEventListener("input", (e) => {
  const value = e.target.value
  for( let i= 0 ; i < card_titles.length ; i++){

        if(card_titles[i].textContent.includes(value) && value.length >= 3 ){
card_content.style.display=" block"
          card_paernts[i].style.display="block";
        } else{
          card_paernts[i].style.display="none";
        }
        
  
      }
  

})


const toastLiveExample2 = document.getElementById('liveToast2');
const toast2 = new bootstrap.Toast(toastLiveExample2)

  for( let n = 0 ; n < mygivebuttons.length ; n++){
    mygivebuttons[n].addEventListener('click', (event) => {
      toast2.show()
    });
  }
  




// wishing list end 


// ------------------------------- add-donation-end














































