---
layout: post 
title: Project Bitshift
description: "Description Here"
author: Spencer Lyons, Xavier Thompson, Justin Quach
hide: true
menu: nav/home.html
---

<style>
  body {
    margin: 0;
    background: #111;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: sans-serif;
  }
  .carousel {
    width: 600px;
    height: 300px;
    overflow: hidden;
    position: relative;
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
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255, 255, 255, 0.2);
    border: none;
    color: white;
    font-size: 2rem;
    padding: 0.2em 0.5em;
    cursor: pointer;
    z-index: 2;
    border-radius: 8px;
    transition: background 0.3s;
  }
  .arrow:hover {
    background: rgba(255, 255, 255, 0.4);
  }
  .arrow.left {
    left: 10px;
  }
  .arrow.right {
    right: 10px;
  }
</style>

<div class="carousel">
  <button class="arrow left">&#8592;</button>
  <div class="carousel-track">
    <img src="images/binary/color_code.png" class="slide" />
    <img src="images/binary/color_code.png" class="slide" />
    <img src="images/binary/color_code.png" class="slide" />
    <img src="images/binary/color_code.png" class="slide" />
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

## Hands On Binary

This project is designed to teach binary in an engaging and interactive way using a hands-on 3D environment. Rather than relying on abstract concepts or traditional memorization, users will learn by directly manipulating objects that represent binary values. Whether it's flipping switches, stacking blocks, or activating machines, each action visually reinforces how binary works in computers. The goal is to make binary accessible to everyone—especially those who find the concept confusing at first but are curious and eager to understand how it powers the digital world around them.