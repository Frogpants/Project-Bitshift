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
    margin-bottom: 1rem;
  }

  .inputs input {
    padding: 10px 16px;
    font-size: 1.2rem;
    border: none;
    border-radius: 10px;
    outline: none;
    width: 180px;
  }

  .bit-box, .place-value-table {
    display: flex;
    justify-content: center;
    margin-bottom: 1rem;
    gap: 10px;
    flex-wrap: wrap;
  }

  .bit, .place {
    padding: 10px;
    width: 40px;
    text-align: center;
    font-weight: bold;
    border-radius: 6px;
  }

  .bit.on {
    background: #27ae60;
  }

  .bit.off {
    background: #7f8c8d;
  }

  .place {
    background: #2c2c40;
    color: #f9ca24;
  }

  .explanation {
    max-width: 700px;
    background: #2d2d44;
    padding: 20px;
    border-radius: 12px;
    line-height: 1.6;
    margin-bottom: 1rem;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 15px;
    width: 100%;
    max-width: 800px;
    margin-bottom: 2rem;
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
  const maxCard = 10;
  const inputMax = 128;

  const title = document.createElement("h1");
  const decInput = document.createElement("input");
  const binInput = document.createElement("input");
  const inputContainer = document.createElement("div");
  const grid = document.createElement("div");
  const explanation = document.createElement("div");
  const bitBox = document.createElement("div");
  const placeValueTable = document.createElement("div");

  title.textContent = "Decimal ↔ Binary Visualizer";
  inputContainer.className = "inputs";
  grid.className = "grid";
  explanation.className = "explanation";
  bitBox.className = "bit-box";
  placeValueTable.className = "place-value-table";

  decInput.placeholder = "Enter Decimal (0–128)";
  binInput.placeholder = "Enter Binary";

  inputContainer.appendChild(decInput);
  inputContainer.appendChild(binInput);
  document.body.appendChild(title);
  document.body.appendChild(inputContainer);
  document.body.appendChild(placeValueTable);
  document.body.appendChild(bitBox);
  document.body.appendChild(explanation);
  document.body.appendChild(grid);

  function decToBin(dec) {
    return (dec >>> 0).toString(2);
  }

  function binToDec(bin) {
    return parseInt(bin, 2);
  }

  function updateHighlight(value) {
    [...grid.children].forEach(card => {
      card.classList.remove("active");
      if (parseInt(card.dataset.dec) === value) {
        card.classList.add("active");
      }
    });
  }

  function updateExplanation(dec) {
    if (isNaN(dec) || dec < 0 || dec > inputMax) {
      explanation.textContent = "Enter a number between 0 and 128.";
      bitBox.innerHTML = "";
      placeValueTable.innerHTML = "";
      return;
    }

    const bin = decToBin(dec).padStart(8, "0");
    const places = [128, 64, 32, 16, 8, 4, 2, 1];

    // Create visual bits
    let bitsHTML = "";
    let mathExp = "";

    for (let i = 0; i < bin.length; i++) {
      const bitVal = places[i];
      const on = bin[i] === "1";
      bitsHTML += `<div class="bit ${on ? "on" : "off"}">${bin[i]}</div>`;
      if (on) {
        mathExp += (mathExp ? " + " : "") + `1×${bitVal}`;
      }
    }

    bitBox.innerHTML = bitsHTML;

    // Create place value labels
    placeValueTable.innerHTML = places.map(p => `<div class="place">${p}</div>`).join("");

    explanation.innerHTML = `<strong>${dec}</strong> in binary is <strong>${bin}</strong><br>It equals: ${mathExp || "0"}`;
  }

  decInput.addEventListener("input", () => {
    const val = parseInt(decInput.value);
    if (!isNaN(val) && val >= 0 && val <= inputMax) {
      binInput.value = decToBin(val);
      updateHighlight(val);
      updateExplanation(val);
    } else {
      binInput.value = "";
      updateHighlight(-1);
      updateExplanation(NaN);
    }
  });

  binInput.addEventListener("input", () => {
    const val = binInput.value;
    if (/^[01]+$/.test(val)) {
      const dec = binToDec(val);
      if (dec <= inputMax) {
        decInput.value = dec;
        updateHighlight(dec);
        updateExplanation(dec);
      } else {
        decInput.value = "";
        explanation.textContent = "Value exceeds 128.";
      }
    } else {
      decInput.value = "";
      updateHighlight(-1);
      updateExplanation(NaN);
    }
  });

  for (let i = 0; i <= maxCard; i++) {
    const card = document.createElement("div");
    card.className = "card";
    card.dataset.dec = i;
    card.innerHTML = `<strong>${i}</strong><span>${decToBin(i)}</span>`;
    card.addEventListener("click", () => {
      decInput.value = i;
      binInput.value = decToBin(i);
      updateHighlight(i);
      updateExplanation(i);
    });
    grid.appendChild(card);
  }

  updateExplanation(NaN);
</script>
