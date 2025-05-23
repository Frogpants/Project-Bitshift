---
layout: post
title: 
search_exclude: true
permalink: /settings
---

<style>
  body {
    font-family: 'Segoe UI', sans-serif;
    padding: 40px 20px;
    transition: background 0.3s, color 0.3s;
  }

  #settings-container {
    max-width: 700px;
    margin: 0 auto;
    padding: 24px;
    border-radius: 18px;
    transition: background 0.3s, box-shadow 0.3s;
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

  #storage-table input {
    padding: 8px;
    width: 100%;
    border-radius: 6px;
    font-size: 0.95rem;
    transition: 0.2s;
  }

  .action-btn {
    padding: 6px 12px;
    border-radius: 6px;
    border: none;
    color: white;
    cursor: pointer;
    font-size: 0.85rem;
    transition: background 0.2s ease;
  }

  .clear-all-btn {
    display: block;
    margin: 12px auto;
    border: none;
    padding: 12px 20px;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.3s ease;
  }

  .no-data {
    text-align: center;
    padding: 20px 0;
    font-style: italic;
  }

  #storage-table tr:hover td {
    background-color: #1e1e1e;
  }

  #storage-table input:focus {
    outline: none;
    border: 1px solid #00c6ff;
  }

  .action-btn::before {
    content: "🗑 ";
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

  /* DARK MODE */
  body.dark-mode {
    background: #121212;
    color: #e0e0e0;
  }

  .dark-mode #settings-container {
    background: #1a1a1a;
    box-shadow: 0 0 20px rgba(0, 200, 255, 0.15);
  }

  .dark-mode #storage-table th {
    color: #00c6ff;
  }

  .dark-mode #storage-table input {
    background: #222;
    color: #eee;
    border: 1px solid #333;
  }

  .dark-mode .clear-all-btn {
    background: #00c6ff;
    color: white;
  }

  .dark-mode .clear-all-btn:hover {
    background: #009cd3;
  }

  .dark-mode .action-btn {
    background: #ff4081;
  }

  .dark-mode .action-btn:hover {
    background: #e63670;
  }

  .dark-mode .no-data {
    color: #888;
  }

  /* LIGHT MODE */
  body.light-mode {
    background: #f5f5f5;
    color: #222;
  }

  .light-mode #settings-container {
    background: #ffffff;
    box-shadow: 0 0 20px rgba(0, 100, 255, 0.08);
  }

  .light-mode #storage-table th {
    color: #0066cc;
  }

  .light-mode #storage-table input {
    background: #f0f0f0;
    color: #222;
    border: 1px solid #ccc;
  }

  .light-mode .clear-all-btn {
    background: #0066cc;
    color: white;
  }

  .light-mode .clear-all-btn:hover {
    background: #0050a0;
  }

  .light-mode .action-btn {
    background: #ff5c8d;
  }

  .light-mode .action-btn:hover {
    background: #d9446f;
  }

  .light-mode .no-data {
    color: #666;
  }
</style>

<div id="settings-container">
  <h2>Your Preferences</h2>
  <p class="description">Below are your saved preferences in this browser. You can delete items or clear everything.</p>

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
  <button class="clear-all-btn" onclick="toggleTheme()">Toggle Light/Dark Mode</button>
</div>

<script>
  function applyTheme(theme) {
    document.body.classList.remove("light-mode", "dark-mode");
    document.body.classList.add(`${theme}-mode`);
    localStorage.setItem("theme", theme);
    renderStorage(); // Ensure inputs re-render with correct colors
  }

  function toggleTheme() {
    const current = localStorage.getItem("theme") || "dark";
    const newTheme = current === "dark" ? "light" : "dark";
    applyTheme(newTheme);
  }

  function initializeTheme() {
    const saved = localStorage.getItem("theme") || "dark";
    applyTheme(saved);
  }

  function renderStorage() {
    const tbody = document.querySelector("#storage-table tbody");
    tbody.innerHTML = "";

    if (localStorage.length === 0 || (localStorage.length === 1 && localStorage.getItem("theme"))) {
      tbody.innerHTML = `<tr><td colspan="3" class="no-data">No progress made yet :(</td></tr>`;
    }

    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (key === "theme") continue;

      const value = localStorage.getItem(key);

      const row = document.createElement("tr");
      row.innerHTML = `
        <td>Progress</td>
        <td><input value="${value}" onchange="updateItem('${key}', this.value)"></td>
        <td><button class="action-btn" onclick="deleteItem('${key}')">Delete</button></td>
      `;
      tbody.appendChild(row);
    }

    // Show theme setting separately
    const themeRow = document.createElement("tr");
    const currentTheme = localStorage.getItem("theme") || "dark";
    themeRow.innerHTML = `
      <td>Theme</td>
      <td><input value="${currentTheme}" disabled></td>
      <td><em>Active</em></td>
    `;
    tbody.appendChild(themeRow);
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
    if (confirm("Clear all saved data? This cannot be undone.")) {
      localStorage.clear();
      localStorage.setItem("theme", "dark"); // Reset to dark
      renderStorage();
      applyTheme("dark");
    }
  }

  window.addEventListener("load", () => {
    initializeTheme();
    renderStorage();
  });
</script>


If you'd like to learn more about our project and how it works, look out our resource page [here](https://github.com/Frogpants/Project-Bitshift/issues/3).
