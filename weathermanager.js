iso = document.getElementById('ISO');
monannul = document.getElementById('monannul');
yearRange = document.getElementById('year-range');

submitButton = document.getElementById('submit');
submitButton.addEventListener('click', changeStats);

function changeStats() {
    console.log(iso.innerHTML + " " + monannul.innerHTML + " " + yearRange.innerHTML);
}