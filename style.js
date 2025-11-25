
const light = "#cfccc6";
const dark = "#242526";

changeColourMode = function() {
    if (document.getElementById("darkMode").checked) {
        document.documentElement.style.setProperty('--textcol', light);
        document.documentElement.style.setProperty('--bgcol', dark);
    } else {
        document.documentElement.style.setProperty('--textcol', dark);
        document.documentElement.style.setProperty('--bgcol', light);
    }
}

// window.onload <- function() {
//     console.log("Hello")
//     console.log(window.innerWidth)
//     if (window.innerWidth < 1000) {
//         console.log("On mobile!")
//         document.documentElement.style.setProperty('--smalltext', '36pt');
//         document.documentElement.style.setProperty('--mediumtext', '72pt');
//         document.documentElement.style.setProperty('--largetext', '162pt');
//     } else {
//         console.log("Not on mobile!")
//     }
// }

