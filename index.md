---
layout: post
title:
description:
author:
hide: true
menu: nav/home.html
---

<style>
  body.fade-out {
    opacity: 0;
    transition: opacity 1s ease;
  }

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
    overflow: hidden;
    transition: background-color 0.4s ease;
  }

  .circle:hover {
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
    pointer-events: none;
    z-index: 2;
  }

  .particle {
    position: absolute;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: white;
    pointer-events: none;
    z-index: 1;
    animation: particle-explode 0.8s ease-out forwards;
  }

  @keyframes particle-explode {
    0% {
      transform: translate(0, 0) scale(1);
      opacity: 1;
    }
    100% {
      transform: translate(var(--x), var(--y)) scale(0.5);
      opacity: 0;
    }
  }
</style>

<div style="text-align: center;">
  <div class="circle" id="startButton">
    <div class="text">Begin Experience</div>
  </div>
</div>

<script>
  const button = document.getElementById("startButton");

  button.addEventListener("click", () => {
    // Particle explosion
    for (let i = 0; i < 50; i++) {
      const particle = document.createElement("div");
      particle.className = "particle";

      // Random position
      const angle = Math.random() * 2 * Math.PI;
      const radius = Math.random() * 150 + 50;
      const x = Math.cos(angle) * radius + "px";
      const y = Math.sin(angle) * radius + "px";

      particle.style.setProperty("--x", x);
      particle.style.setProperty("--y", y);

      // Random start position inside button
      const rect = button.getBoundingClientRect();
      particle.style.left = rect.left + rect.width / 2 + "px";
      particle.style.top = rect.top + rect.height / 2 + "px";

      document.body.appendChild(particle);

      // Remove after animation
      setTimeout(() => particle.remove(), 800);
    }

    // Fade out entire page
    document.body.classList.add("fade-out");

    // Navigate after animation
    setTimeout(() => {
      window.location.href = "https://frogpants.github.io/Project-Bitshift/original-renders/First-Demo-Project.html";
    }, 1000);
  });
</script>

Make sure to check out our Github Page!