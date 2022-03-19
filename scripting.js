

const search = document.getElementById('search');
const q = document.getElementById('query');
const thegoog = 'https://www.google.com/search?q=site%3A+';
//const filePath = 'file:///Users/niaalvarado/Cs90/product.html?q='; WILL search site once completed I just dont have 
// enough content right now to make it searchable 

function submitted(event) {
    event.preventDefault();
    const url = thegoog + '+' + q.value;
    const windo = window.open(url, '_blank');
    windo.focus();
}
//Do not need any validation of input since it searches only google right now
//Add validation to searchable content after it is added 


search.addEventListener('submit', submitted);


// Absolute garbage page literally did nothing much of my own but connect it and double check I understood it myself 

// What will I be adding??? The mini games I will have on each page will be held in this file and the further scripting 
// will be on the other pages 
// I am currently researching what else to add while making the page practical. I want to replace this with a modified code
// as well to be able to do more and not connect so badly. 






