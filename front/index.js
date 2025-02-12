
const url = "http://192.168.0.182:8000/arduino/"


window.onload = function () {
  const container = document.getElementById("buttons-container");

  for (let i = 0; i <= 9; i++) {
    let button = document.createElement("button");
    button.textContent = i;
    button.onclick = () => {
        blink(i)
    };
    container.appendChild(button);
  }
};

async function blink(numero) {
    url_post = url + numero

    try {
        let response = await fetch(url_post);
        let data = await response.text();
        alert(data)
    } catch (error) {
        console.error('Error:', error);
    }
}
