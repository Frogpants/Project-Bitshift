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
    width: 700px;
  }

  .carousel-window {
    width: 660px;
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
    transition: all 0.5s ease;
    filter: blur(2px);
    opacity: 0.5;
    transform: scale(0.8);
    border-radius: 12px;
    object-fit: cover;
  }

  .slide.active {
    filter: none;
    opacity: 1;
    transform: scale(1.2);
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
    margin-bottom: 40px;
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

  body.fade-out {
    opacity: 0;
  }
</style>

<div class="circle" id="startButton">
  <div class="text">Begin Experience</div>
</div>

<div class="carousel">
  <button class="arrow left">&#8592;</button>
  <div class="carousel-window">
    <div class="carousel-track">
      <img src="images/binary/color_code.png" class="slide" />
      <img src="images/binary/color_code.png" class="slide" />
      <img src="images/binary/color_code.png" class="slide" />
      <img src="images/binary/color_code.png" class="slide" />
    </div>
  </div>
  <button class="arrow right">&#8594;</button>
</div>

<script>
  const slides = document.querySelectorAll('.slide');
  const leftBtn = document.querySelector('.arrow.left');
  const rightBtn = document.querySelector('.arrow.right');
  let index = 0;
  let autoSlide;

  function updateSlides() {
    slides.forEach((slide, i) => {
      slide.classList.remove('active');
      if (i === index) {
        slide.classList.add('active');
      }
    });

    const track = document.querySelector('.carousel-track');
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

  function resetAutoSlide() {
    clearInterval(autoSlide);
    autoSlide = setInterval(nextSlide, 3000);
  }

  autoSlide = setInterval(nextSlide, 3000);
  updateSlides();
</script>

<p style="text-align: center; margin-top: 40px;">Make sure to check out our <a href="https://github.com/frogpants/Project-Bitshift" target="_blank" style="color: #42a5f5;">GitHub Page</a>!</p>
