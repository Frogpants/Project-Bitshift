---
layout: post
title:
description:
author:
hide: true
menu: nav/home.html
---

<style>
  body {
    font-family: 'Segoe UI', sans-serif;
    background: #1e1e1e;
    color: #eee;
    margin: 0;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .carousel {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 40px 0 20px;
    width: 100%;
    max-width: 900px;
  }

  .carousel-window {
    width: 100%;
    overflow: hidden;
  }

  .carousel-track {
    display: flex;
    transition: transform 0.6s cubic-bezier(0.77, 0, 0.175, 1);
  }

  .slide {
    width: 200px;
    height: 200px;
    margin: 0 10px;
    opacity: 0.4;
    transform: scale(0.8);
    transition: all 0.4s ease-in-out;
    border-radius: 12px;
    object-fit: cover;
    cursor: pointer;
    filter: brightness(0.7);
  }

  .slide.active {
    opacity: 1;
    transform: scale(1.1);
    filter: brightness(1) drop-shadow(0 0 10px rgba(255,255,255,0.15));
    z-index: 1;
  }

  .arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0, 0, 0, 0.5);
    border: none;
    font-size: 2rem;
    color: #eee;
    cursor: pointer;
    padding: 10px 15px;
    border-radius: 50%;
    z-index: 2;
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .carousel:hover .arrow {
    opacity: 1;
  }

  .arrow.left {
    left: 10px;
  }

  .arrow.right {
    right: 10px;
  }

  .dots {
    display: flex;
    justify-content: center;
    margin-top: 14px;
    gap: 10px;
  }

  .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background-color: #555;
    transition: background-color 0.3s ease;
    cursor: pointer;
  }

  .dot.active {
    background-color: #fff;
  }

  /* Modal Overlay */
  .modal {
    display: flex;
    position: fixed;
    z-index: 9999;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.9);
    justify-content: center;
    align-items: center;
    padding: 40px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.4s ease;
  }

  .modal.visible {
    opacity: 1;
    pointer-events: auto;
  }

  .modal-image {
    width: auto;
    height: auto;
    max-width: 700px;
    max-height: 80vh;
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
    transform: scale(0.9);
    opacity: 0;
    transition: transform 0.5s ease, opacity 0.5s ease;
  }

  .modal.visible .modal-image {
    transform: scale(1);
    opacity: 1;
  }

  .close {
    position: absolute;
    top: 20px;
    right: 30px;
    font-size: 32px;
    color: white;
    cursor: pointer;
  }

  .binary-anim {
    font-family: monospace;
    font-size: 1.2rem;
    text-align: center;
    margin-top: 40px;
    color: #89caff;
    letter-spacing: 1px;
    min-height: 1.5em;
    white-space: nowrap;
    overflow: hidden;
    position: relative;
  }

  .binary-anim::after {
    content: "|";
    animation: blink 1s step-end infinite;
    position: absolute;
    right: -10px;
    top: 0;
    color: #89caff;
  }

  @keyframes blink {
    50% {
      opacity: 0;
    }
  }

  .parallax-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.07) 1px, transparent 1px),
              radial-gradient(circle, rgba(255,255,255,0.07) 1px, transparent 1px);
  background-position: 0 0, 25px 25px;
  background-size: 50px 50px;
  z-index: -1;
  animation: drift 60s linear infinite;
  opacity: 0.25;
  pointer-events: none;
}

@keyframes drift {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(-100px, -100px);
  }
}

  .controls-panel {
  margin-top: 50px;
  padding: 20px 30px;
  background: #181818;
  border: 1px solid #2a2a2a;
  border-radius: 12px;
  color: #ccc;
  max-width: 600px;
  text-align: left;
  box-shadow: 0 0 20px rgba(137, 202, 255, 0.05);
}

.controls-panel h2 {
  color: #89caff;
  font-size: 1.2rem;
  margin-bottom: 10px;
  font-family: 'Segoe UI', monospace;
}

.controls-panel ul {
  list-style: none;
  padding-left: 0;
  margin: 0;
}

.controls-panel li {
  margin: 8px 0;
  font-size: 0.95rem;
  font-family: monospace;
}

kbd {
  background: #333;
  color: #89caff;
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 0.85rem;
  margin: 0 2px;
  display: inline-block;
}

.centered-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  margin-top: 40px;
  text-align: center;
}

  .items-dictionary-wrapper {
  margin-top: 50px;
  max-width: 600px;
  text-align: center;
}

.toggle-items {
  background-color: #111;
  color: #89caff;
  border: 2px solid #89caff;
  padding: 10px 20px;
  font-family: monospace;
  font-size: 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.toggle-items:hover {
  background-color: #1f2a38;
  color: white;
  transform: scale(1.02);
}

.items-index {
  margin-top: 20px;
  padding: 20px 30px;
  background: #181818;
  border: 1px solid #2a2a2a;
  border-radius: 12px;
  color: #ccc;
  text-align: left;
  box-shadow: 0 0 20px rgba(137, 202, 255, 0.05);
  font-family: monospace;
}

.items-index h2 {
  color: #89caff;
  font-size: 1.2rem;
  margin-bottom: 14px;
}

.items-index ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.items-index li {
  margin-bottom: 18px;
  line-height: 1.4;
}

.item-desc {
  color: #aaa;
  font-size: 0.9rem;
}

</style>


<div class="parallax-bg"></div>

<!-- Carousel -->
<div class="carousel">
  <button class="arrow left">&#8592;</button>
  <div class="carousel-window">
    <div class="carousel-track">
      <img src="images/binary/screenshots/main-screen.png" class="slide" loading="lazy" />
      <img src="images/binary/screenshots/settings-screen.png" class="slide" loading="lazy" />
      <img src="images/binary/screenshots/scene-1.png" class="slide" loading="lazy" />
      <img src="images/binary/screenshots/scene-2.png" class="slide" loading="lazy" />
      <img src="images/binary/screenshots/scene-3.png" class="slide" loading="lazy" />
      <img src="images/binary/screenshots/puzzle-screen.png" class="slide" loading="lazy" />
      <img src="images/binary/screenshots/epic-scene-1.png" class="slide" loading="lazy" />
    </div>
  </div>
  <button class="arrow right">&#8594;</button>
</div>

<!-- Dots -->
<div class="dots">
  <span class="dot active"></span>
  <span class="dot"></span>
  <span class="dot"></span>
  <span class="dot"></span>
  <span class="dot"></span>
  <span class="dot"></span>
  <span class="dot"></span>
</div>

<!-- Fullscreen Modal -->
<div class="modal" id="imageModal">
  <span class="close">&times;</span>
  <img class="modal-image" id="modalImg" />
</div>

<div class="centered-container">
  <!-- Fullscreen Modal -->
  <div class="modal" id="imageModal">
    <span class="close">&times;</span>
    <img class="modal-image" id="modalImg" />
  </div>

  <!-- Controls Panel -->
  <div class="controls-panel">
    <h2>Controls</h2>
    <ul>
      <li><kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> — Move</li>
      <li><kbd>↑</kbd> <kbd>↓</kbd> <kbd>←</kbd> <kbd>→</kbd> — Look around</li>
      <li><kbd>Space</kbd> — Enter binary puzzle</li>
      <li><kbd>F</kbd> — Toggle flashlight</li>
      <li><kbd>Q</kbd> — Open walkie talkie</li>
      <li><kbd>Esc</kbd> — Close or pause</li>
      <li><kbd>Click</kbd> — Interact</li>
    </ul>
  </div>
</div>

<div class="items-dictionary-wrapper">
  <button class="toggle-items" onclick="toggleItems()">Open Tech & Items Dictionary</button>

  <div class="items-index" id="itemsIndex" style="display: none;">
    <h2>In-Game Tech & Items Index</h2>
    <ul>
      <li>
        <strong>Flashlight</strong><br>
        <span class="item-desc">Used to illuminate dark data zones. Essential for low-visibility puzzles. Toggle with <kbd>F</kbd>.</span>
      </li>
      <li>
        <strong>Walkie Talkie</strong><br>
        <span class="item-desc">Enables encrypted comms between agents. Used to receive puzzle hints and lore drops. Activate with <kbd>Q</kbd>.</span>
      </li>
      <li>
        <strong>Binary Decoder</strong><br>
        <span class="item-desc">Auto-scrolls through binary strings to highlight anomalies. Acquired after Puzzle 2.</span>
      </li>
      <li>
        <strong>Access Key</strong><br>
        <span class="item-desc">Unlocks restricted puzzle nodes. One-time use item found in hidden scenes.</span>
      </li>
      <li>
        <strong>Logic Probe</strong><br>
        <span class="item-desc">Allows real-time scanning of logical flowcharts. Reveals gate structures.</span>
      </li>
    </ul>
  </div>
</div>


<!-- Footer -->
<p style="text-align: center; margin-top: 30px;">
  View the full project on <a href="https://github.com/frogpants/Project-Bitshift" target="_blank" style="color: #89caff;">GitHub</a>.
</p>




<script>
  const slides = document.querySelectorAll('.slide');
  const dots = document.querySelectorAll('.dot');
  const track = document.querySelector('.carousel-track');
  const leftBtn = document.querySelector('.arrow.left');
  const rightBtn = document.querySelector('.arrow.right');
  const carousel = document.querySelector('.carousel');
  const modal = document.getElementById("imageModal");
  const modalImg = document.getElementById("modalImg");
  const closeBtn = document.querySelector(".close");

  let index = 0;
  let autoSlide;

  function updateSlides() {
    slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === index);
    });
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === index);
    });

    const offset = (index * -220) + (carousel.offsetWidth / 2 - 110);
    track.style.transform = `translateX(${offset}px)`;
  }

  function nextSlide() {
    index = (index + 1) % slides.length;
    updateSlides();
  }

  function prevSlide() {
    index = (index - 1 + slides.length) % slides.length;
    updateSlides();
  }

  leftBtn.addEventListener('click', () => {
    prevSlide();
    resetAutoSlide();
  });

  rightBtn.addEventListener('click', () => {
    nextSlide();
    resetAutoSlide();
  });

  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      index = i;
      updateSlides();
      resetAutoSlide();
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') {
      nextSlide();
      resetAutoSlide();
    } else if (e.key === 'ArrowLeft') {
      prevSlide();
      resetAutoSlide();
    } else if (e.key === 'Escape') {
      modal.classList.remove("visible");
    }
  });

  carousel.addEventListener('mouseenter', () => clearInterval(autoSlide));
  carousel.addEventListener('mouseleave', () => resetAutoSlide());

  function resetAutoSlide() {
    clearInterval(autoSlide);
    autoSlide = setInterval(nextSlide, 3000);
  }

  autoSlide = setInterval(nextSlide, 3000);
  updateSlides();

  // Modal logic
  slides.forEach((slide) => {
    slide.addEventListener("click", () => {
      modalImg.src = slide.src;
      modal.classList.add("visible");
    });
  });

  closeBtn.onclick = () => {
    modal.classList.remove("visible");
  };

  window.addEventListener("click", (event) => {
    if (event.target === modal) {
      modal.classList.remove("visible");
    }
  });

  function toggleItems() {
  const panel = document.getElementById("itemsIndex");
  const btn = document.querySelector(".toggle-items");

  const isOpen = panel.style.display === "block";
  panel.style.display = isOpen ? "none" : "block";
  btn.textContent = isOpen
    ? "Open Tech & Items Dictionary"
    : "Close Tech & Items Dictionary";
}

</script>
