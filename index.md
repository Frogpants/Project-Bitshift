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
    background: #f5f5f5;
    color: #333;
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
    color: #333;
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
    background-color: #aaa;
    cursor: pointer;
  }

  .dot.active {
    background-color: #333;
  }

  /* Modal Styles with Transitions */
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
    transition: opacity 0.4s ease;
  }

  .modal.visible {
    opacity: 1;
    pointer-events: auto;
  }

  .modal-image {
    max-width: 90%;
    max-height: 90%;
    border-radius: 8px;
    transform: scale(0.9);
    transition: transform 0.4s ease, opacity 0.4s ease;
    opacity: 0;
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

<p style="text-align: center; margin-top: 30px;">
  View the full project on <a href="https://github.com/frogpants/Project-Bitshift" target="_blank">GitHub</a>.
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

  // Modal logic with transitions
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
</script>
