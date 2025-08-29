document.getElementById("dataForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;

  const response = await fetch("http://127.0.0.1:5000/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email })
  });

  const result = await response.json();

  if (result.status === "success") {
    window.location.href = "success.html"; // redirect
  } else {
    document.getElementById("message").textContent = "Error: " + result.message;
  }
});
