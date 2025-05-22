---
layout: post
title: Binary
search_exclude: true
menu: nav/home.html
---

<style>
  body {
    font-family: 'Segoe UI', sans-serif;
    background: #1e1e2f;
    color: #fff;
    margin: 0;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
    color: #f9ca24;
  }

  .inputs {
    display: flex;
    gap: 20px;
    margin-bottom: 2rem;
  }

  .inputs input {
    padding: 10px 16px;
    font-size: 1.2rem;
    border: none;
    border-radius: 10px;
    outline: none;
    width: 180px;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 15px;
    width: 100%;
    max-width: 800px;
  }

  .card {
    background: #2c2c40;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    cursor: pointer;
    transition: transform 0.2s, background 0.3s;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
  }

  .card:hover {
    transform: scale(1.05);
    background: #40406b;
  }

  .card.active {
    background: #00cec9;
    color: #000;
  }

  .card span {
    display: block;
    font-size: 1.2rem;
    margin-top: 8px;
    color: #bbb;
  }
</style>

<script>
  const max = 10;

  const decInput = document.createElement("input");
  const binInput = document.createElement("input");
  const inputContainer = document.createElement("div");
  const grid = document.createElement("div");
  const title = document.createElement("h1");

  title.textContent = "Decimal ↔ Binary Visualizer";
  inputContainer.className = "inputs";
  grid.className = "grid";
  decInput.placeholder = "Enter Decimal";
  binInput.placeholder = "Enter Binary";

  inputContainer.appendChild(decInput);
  inputContainer.appendChild(binInput);
  document.body.appendChild(title);
  document.body.appendChild(inputContainer);
  document.body.appendChild(grid);

  function updateHighlight(value) {
    [...grid.children].forEach(card => {
      card.classList.remove("active");
      if (parseInt(card.dataset.dec) === value) {
        card.classList.add("active");
      }
    });
  }

  function decToBin(dec) {
    return (dec >>> 0).toString(2);
  }

  function binToDec(bin) {
    return parseInt(bin, 2);
  }

  decInput.addEventListener("input", () => {
    const val = parseInt(decInput.value);
    if (!isNaN(val) && val >= 0 && val <= max) {
      binInput.value = decToBin(val);
      updateHighlight(val);
    } else {
      binInput.value = "";
      updateHighlight(-1);
    }
  });

  binInput.addEventListener("input", () => {
    const val = binInput.value;
    if (/^[01]+$/.test(val)) {
      const dec = binToDec(val);
      decInput.value = dec;
      updateHighlight(dec);
    } else {
      decInput.value = "";
      updateHighlight(-1);
    }
  });

  for (let i = 0; i <= max; i++) {
    const card = document.createElement("div");
    card.className = "card";
    card.dataset.dec = i;
    card.innerHTML = `<strong>${i}</strong><span>${decToBin(i)}</span>`;
    card.addEventListener("click", () => {
      decInput.value = i;
      binInput.value = decToBin(i);
      updateHighlight(i);
    });
    grid.appendChild(card);
  }
</script>


