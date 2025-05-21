---
layout: post
title:
description:
author:
hide: true
menu: nav/home.html
---

<style>
  .circle {
    height: 300px;
    width: 300px;
    background-color: #1e3c72;
    border-radius: 15%;
    display: inline-block;
    cursor: pointer;
    position: relative;
    box-shadow: 0 0 25px rgba(50, 100, 255, 0.3), 0 0 60px rgba(150, 50, 255, 0.2);
    border: 2px solid rgba(255, 255, 255, 0.1);
    transition: transform 0.4s ease-in-out, background-color 0.6s ease-in-out, box-shadow 0.4s;
    overflow: hidden;
  }

  .circle:hover {
    transform: scale(1.08);
    background-color: #8e24aa;
    box-shadow: 0 0 30px rgba(142, 36, 170, 0.5), 0 0 70px rgba(142, 36, 170, 0.3);
  }

  .text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-weight: bold;
    color: white;
    font-size: 1.6em;
    text-shadow: 0 0 5px rgba(255, 255, 255, 0.2);
    transition: color 0.3s ease-in-out;
    text-align: center;
  }

  .circle:hover .text {
    color: #f3e5f5;
    text-shadow: 0 0 12px #ffffff, 0 0 25px #ce93d8;
  }

  @keyframes explode {
    0% {
      transform: scale(1);
      opacity: 1;
      box-shadow: 0 0 25px rgba(255, 255, 255, 0.3);
    }
    50% {
      transform: scale(2);
      opacity: 0.8;
      box-shadow: 0 0 60px rgba(255, 0, 150, 0.5);
    }
    100% {
      transform: scale(3);
      opacity: 0;
      box-shadow: 0 0 120px rgba(255, 0, 150, 0.0);
    }
  }

  .explode {
    animation: explode 0.6s ease-out forwards;
    pointer-events: none;
  }
</style>

<div style="text-align: center;">
  <div class="circle" id="startButton">
    <div class="text">
      <p>Begin Experience</p>
    </div>
  </div>
</div>

<script>
  const button = document.getElementById("startButton");

  button.addEventListener("click", () => {
    button.classList.add("explode");

    // Wait for explosion to finish, then redirect
    setTimeout(() => {
      window.location.href = "navigation/section/game.md";
    }, 600); // matches animation duration
  });
</script>
