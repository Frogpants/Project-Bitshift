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
    background: #121212;
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
    max-width: 700px;
  }

  .carousel-window {
    width: 660px;
    max-width: 100%;
    overflow: hidden;
  }

  .carousel-track {
    display: flex;
    align-items: center;
    transition: transform 0.5s ease;
  }

  .slide {
    width: 200px;
    height: 200px;
    margin: 0 10px;
    transition: all 0.5s ease, filter 0.3s ease;
    filter: blur(2px);
    opacity: 0.5;
    transform: scale(0.6);
    border-radius: 12px;
    object-fit: cover;
  }

  .slide.active {
    filter: none;
    opacity: 1;
    transform: scale(1);
    z-index: 1;
  }

  .arrow {
    background: none;
    border: none;
    font-size: 2rem;
    color: white;
    cursor: pointer;
    z-index: 2;
  }

  .arrow.left {
    margin-right: 10px;
  }

  .arrow.right {
    margin-left: 10px;
  }

  .dots {
    margin-top: 20px;
    display: flex;
    justify-content: center;
    gap: 8px;
  }

  .dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: white;
    transition: background-color 0.3s ease;
    cursor: pointer;
  }

  .dot.active {
    background-color: #42a5f5;
  }

  @media (max-width: 768px) {
    .slide {
      width: 150px;
      height: 150px;
    }
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
  <a href="https://github.com/frogpants/Project-Bitshift" target="_blank" style="color: #42a5f5;">GitHub Page</a>!
</p>

<script>
  const slides = document.querySelectorAll('.slide');
  const dots = document.querySelectorAll('.dot');
  const track = document.querySelector('.carousel-track');
  const leftBtn = document.querySelector('.arrow.left');
  const rightBtn = document.querySelector('.arrow.right');
  const carousel = document.querySelector('.carousel');

  let index = 0;
  let autoSlide;

  function updateSlides() {
    slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === index);
    });
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === index);
    });

    const offset = (index * -220) + 190;
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
</script>
