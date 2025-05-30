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
    font-family: sans-serif;
    background: #1e1e1e;
    color: #eee;
    margin: 0;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .carousel {
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
    transition: transform 0.4s ease;
  }

  .slide {
    width: 200px;
    height: 200px;
    margin: 0 10px;
    opacity: 0.5;
    transform: scale(0.8);
    transition: all 0.3s ease;
    border-radius: 8px;
    object-fit: cover;
    cursor: pointer;
  }

  .slide.active {
    opacity: 1;
    transform: scale(1);
  }

  .arrow {
    background: none;
    border: none;
    font-size: 2rem;
    color: #eee;
    cursor: pointer;
    padding: 0 10px;
  }

  .dots {
    display: flex;
    justify-content: center;
    margin-top: 10px;
    gap: 8px;
  }

  .dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: #777;
    cursor: pointer;
  }

  .dot.active {
    background-color: #eee;
  }

  /* Modal Styles */
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
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.6s ease;
  }

  .modal.visible {
    opacity: 1;
    pointer-events: auto;
  }

  .modal-image {
    max-width: 90%;
    max-height: 90%;
    border-radius: 8px;
    transform: scale(0.85);
    opacity: 0;
    transition: transform 0.6s ease, opacity 0.6s ease;
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

  /* Binary Text Animation */
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
  }
</style>

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

<!-- Binary Text Animation -->
<div class="binary-anim" id="binaryAnim"></div>

<!-- Footer -->
<p style="text-align: center; margin-top: 30px;">
  View the full project on <a href="https://github.com/frogpants/Project-Bitshift" target="_blank" style="color: #89caff;">GitHub</a>.
</p>

<!-- Fullscreen Modal -->
<div class="modal" id="imageModal">
  <span class="close">&times;</span>
  <img class="modal-image" id="modalImg" />
</div>

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

  // Binary decoding animation
  const binaryTarget = document.getElementById("binaryAnim");
  const finalText = "Project Bitshift Initialized...";
  const delay = 75;

  let output = "";
  let indexText = 0;

  function animateBinary() {
    if (indexText < finalText.length) {
      const char = finalText[indexText];
      const binary = char.charCodeAt(0).toString(2).padStart(8, '0');
      let step = 0;

      const interval = setInterval(() => {
        if (step < binary.length) {
          binaryTarget.textContent = output + binary.slice(0, step + 1).padEnd(8, '█');
          step++;
        } else {
          clearInterval(interval);
          output += char;
          indexText++;
          animateBinary();
        }
      }, delay);
    } else {
      binaryTarget.textContent = output;
    }
  }

  animateBinary();
</script>
