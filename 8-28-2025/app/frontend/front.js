async function sendRequest() {
      let a = document.getElementById("a").value;
      let b = document.getElementById("b").value;

      let response = await fetch("http://127.0.0.1:8000/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ a: parseInt(a), b: parseInt(b) })
      });

      let data = await response.json();
      document.getElementById("result").innerText = data.result;
    }