
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