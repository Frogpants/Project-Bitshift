---
layout: post
title: 
search_exclude: true
permalink: /settings
---

<style>
  body {
    background: #121212;
    color: white;
    font-family: 'Segoe UI', sans-serif;
    padding: 40px 20px;
  }

  #settings-container {
    max-width: 700px;
    margin: 0 auto;
    background: #1c1c1c;
    color: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 0 15px rgba(0, 200, 255, 0.2);
  }

  #settings-container h2 {
    text-align: center;
    margin-bottom: 10px;
  }

  #settings-container p.description {
    text-align: center;
    font-size: 0.95rem;
    color: #aaa;
    margin-bottom: 20px;
  }

  #storage-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }

  #storage-table th,
  #storage-table td {
    padding: 10px;
    border-bottom: 1px solid #333;
    text-align: left;
  }

  #storage-table input {
    background: #222;
    color: white;
    border: none;
    padding: 6px;
    width: 100%;
    border-radius: 6px;
  }

  .action-btn {
    background: #ff4081;
    padding: 5px 10px;
    border-radius: 6px;
    border: none;
    color: white;
    cursor: pointer;
    font-size: 0.9em;
  }

  .clear-all-btn {
    display: block;
    margin: 0 auto;
    background: #00c6ff;
    color: white;
    border: none;
    padding: 10px 16px;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.3s;
  }

  .clear-all-btn:hover {
    background: #009cd3;
  }

  .no-data {
    text-align: center;
    color: #888;
    padding: 20px 0;
  }
</style>

<div id="settings-container">
  <h2>Settings</h2>
  <p class="description">These are settings or progress saved in your browser. You can remove anything you no longer need.</p>

  <table id="storage-table">
    <thead>
      <tr>
        <th>Preference</th>
        <th>Value</th>
        <th>Remove</th>
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
      tbody.innerHTML = `<tr><td colspan="3" class="no-data">No saved preferences found.</td></tr>`;
      return;
    }

    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      const value = localStorage.getItem(key);

      const row = document.createElement("tr");

      row.innerHTML = `
        <td>${key}</td>
        <td><input value="${value}" disabled></td>
        <td>
          <button class="action-btn" onclick="deleteItem('${key}')">Delete</button>
        </td>
      `;
      tbody.appendChild(row);
    }
  }

  function deleteItem(key) {
    if (confirm(`Delete "${key}" from your saved preferences?`)) {
      localStorage.removeItem(key);
      renderStorage();
    }
  }

  function clearAll() {
    if (confirm("Are you sure you want to clear ALL saved preferences?")) {
      localStorage.clear();
      renderStorage();
    }
  }

  window.addEventListener("load", renderStorage);
</script>
