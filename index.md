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
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    transition: opacity 1s ease;
  }

  .carousel {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 40px;
    position: relative;
    width: 90%;
    max-width: 900px;
  }

  .carousel-window {
    width: 100%;
    overflow: hidden;
  }

  .carousel-track {
    display: flex;
    align-items: center;
    transition: transform 0.5s ease-in-out;
    will-change: transform;
  }

  .slide {
    width: 220px;
    height: 220px;
    margin: 0 10px;
    transition: all 0.5s ease;
    filter: blur(2px);
    opacity: 0.4;
    transform: scale(0.75);
    border-radius: 18px;
    object-fit: cover;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.1);
    border: 2px solid transparent;
    cursor: pointer;
  }

  .slide.active {
    filter: none;
    opacity: 1;
    transform: scale(1.15);
    z-index: 2;
    border-color: #00ffe7;
    box-shadow: 0 0 20px #00ffe7aa;
  }

  .arrow {
    background: none;
    border: none;
    font-size: 2.5rem;
    color: #00ffe7;
    cursor: pointer;
    z-index: 3;
    padding: 0 12px;
    transition: transform 0.3s ease, color 0.3s ease;
    text-shadow: 0 0 8px #00ffe7;
  }

  .arrow:hover {
    transform: scale(1.2);
    color: #42a5f5;
  }

  .dots {
    margin-top: 25px;
    display: flex;
    justify-content: center;
    gap: 10px;
  }

  .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background-color: #888;
    opacity: 0.7;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s;
  }

  .dot.active {
    background-color: #00ffe7;
    transform: scale(1.3);
    box-shadow: 0 0 6px #00ffe7aa;
    opacity: 1;
  }

  @media (max-width: 768px) {
    .slide {
      width: 160px;
      height: 160px;
    }

    .arrow {
      font-size: 2rem;
    }
  }

  /* Modal Styles */
  .modal {
    display: none;
    position: fixed;
    z-index: 9999;
    padding-top: 60px;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.95);
    justify-content: center;
    align-items: center;
  }

  .modal-image {
    margin: auto;
    display: block;
    max-width: 95%;
    max-height: 85%;
    border-radius: 12px;
    box-shadow: 0 0 20px #00ffe7aa;
    transition: transform 0.3s ease;
  }

  .close {
    position: absolute;
    top: 25px;
    right: 40px;
    color: #00ffe7;
    font-size: 40px;
    font-weight: bold;
    transition: 0.3s;
    cursor: pointer;
    text-shadow: 0 0 10px #00ffe7;
  }

  .close:hover {
    color: #42a5f5;
  }
</style>

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

<div class="dots">
  <span class="dot active"></span>
  <span class="dot"></span>
  <span class="dot"></span>
  <span class="dot"></span>
  <span class="dot"></span>
  <span class="dot"></span>
  <span class="dot"></span>
</div>

<p style="text-align: center; margin-top: 40px;">
  Make sure to check out our
  <a href="https://github.com/frogpants/Project-Bitshift" target="_blank" style="color: #00ffe7;">GitHub Page</a>!
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

    const offset = (index * -240) + (carousel.offsetWidth / 2 - 110);
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
      modal.style.display = "flex";
      modalImg.src = slide.src;
    });
  });

  closeBtn.onclick = () => {
    modal.style.display = "none";
  };

  window.addEventListener("click", (event) => {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });
</script>
