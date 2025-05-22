---
layout: post
title: 
search_exclude: true
permalink: /settings
---

<style>
  body {
    background: #121212;
    color: #e0e0e0;
    font-family: 'Segoe UI', sans-serif;
    padding: 40px 20px;
  }

  #settings-container {
    max-width: 700px;
    margin: 0 auto;
    background: #1a1a1a;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 0 20px rgba(0, 200, 255, 0.15);
    transition: 0.3s ease;
  }

  #settings-container h2 {
    text-align: center;
    font-size: 1.8rem;
    margin-bottom: 8px;
  }

  #settings-container p.description {
    text-align: center;
    font-size: 1rem;
    color: #aaaaaa;
    margin-bottom: 24px;
  }

  #storage-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 24px;
  }

  #storage-table th,
  #storage-table td {
    padding: 12px;
    border-bottom: 1px solid #333;
    text-align: left;
    vertical-align: middle;
  }

  #storage-table th {
    color: #00c6ff;
  }

  #storage-table input {
    background: #222;
    color: #eee;
    border: 1px solid #333;
    padding: 8px;
    width: 100%;
    border-radius: 6px;
    font-size: 0.95rem;
  }

  .action-btn {
    background: #ff4081;
    padding: 6px 12px;
    border-radius: 6px;
    border: none;
    color: white;
    cursor: pointer;
    font-size: 0.85rem;
    transition: background 0.2s ease;
  }

  .action-btn:hover {
    background: #e63670;
  }

  .clear-all-btn {
    display: block;
    margin: 20px auto 0;
    background: #00c6ff;
    color: white;
    border: none;
    padding: 12px 20px;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.3s ease;
  }

  .clear-all-btn:hover {
    background: #009cd3;
  }

  .no-data {
    text-align: center;
    color: #888;
    padding: 20px 0;
    font-style: italic;
  }

  @media (max-width: 600px) {
    #settings-container {
      padding: 16px;
    }

    #storage-table th, #storage-table td {
      font-size: 0.85rem;
    }

    .action-btn, .clear-all-btn {
      width: 100%;
      margin-top: 10px;
    }
  }
    /* Fade-in animation on load */
  #settings-container {
    animation: fadeIn 0.6s ease;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  /* Row hover effect for visual feedback */
  #storage-table tr:hover td {
    background-color: #1e1e1e;
  }

  /* Slight input highlight on focus */
  #storage-table input:focus {
    outline: none;
    border: 1px solid #00c6ff;
    background-color: #292929;
  }

  /* Smooth transitions for inputs and buttons */
  #storage-table input,
  .action-btn,
  .clear-all-btn {
    transition: all 0.25s ease;
  }

  /* Action button icon suggestion (optional) */
  .action-btn::before {
    content: "🗑 ";
  }

  /* Clear button hover upgrade */
  .clear-all-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 0 8px rgba(0, 198, 255, 0.5);
  }

  /* Table column alignment tweak */
  #storage-table td:first-child {
    font-weight: 500;
  }

  /* Better spacing for mobile buttons */
  @media (max-width: 600px) {
    .action-btn {
      margin-top: 8px;
    }
  }
</style>

<div id="settings-container">
  <h2>Your Preferences</h2>
  <p class="description">Below are your saved preferences in this browser. You can delete individual items or clear everything.</p>

  <table id="storage-table">
    <thead>
      <tr>
        <th>Setting</th>
        <th>Current Value</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>

  <button class="clear-all-btn" onclick="clearAll()">Clear All Preferences</button>
</div>

<script>
  function renderStorage() {
    const tbody = document.querySelector("#storage-table tbody");
    tbody.innerHTML = "";

    if (localStorage.length === 0) {
      tbody.innerHTML = `<tr><td colspan="3" class="no-data">Nothing saved yet 💤</td></tr>`;
      return;
    }

    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      const value = localStorage.getItem(key);

      const row = document.createElement("tr");

      row.innerHTML = `
        <td>${key}</td>
        <td><input value="${value}" onchange="updateItem('${key}', this.value)"></td>
        <td>
          <button class="action-btn" onclick="deleteItem('${key}')">Delete</button>
        </td>
      `;
      tbody.appendChild(row);
    }
  }

  function updateItem(key, newValue) {
    localStorage.setItem(key, newValue);
  }

  function deleteItem(key) {
    if (confirm(`Are you sure you want to remove "${key}"?`)) {
      localStorage.removeItem(key);
      renderStorage();
    }
  }

  function clearAll() {
    if (confirm("Clear all preferences? This cannot be undone.")) {
      localStorage.clear();
      renderStorage();
    }
  }

  window.addEventListener("load", renderStorage);
</script>
