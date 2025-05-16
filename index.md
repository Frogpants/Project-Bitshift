---
layout: post 
title: Project Bitshift
description: "Description Here"
author: Spencer Lyons, Xavier Thompson, Justin Quach
hide: true
menu: nav/home.html
---

<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Smooth Slideshow</title>
  <style>
    body {
      margin: 0;
      background: #111;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
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
  </style>
</head>
<body>

  <div class="carousel">
    <div class="carousel-track">
      <img src="images/binary/color_code.png" class="slide" />
      <img src="images/binary/color_code.png" class="slide" />
      <img src="images/binary/color_code.png" class="slide" />
      <img src="images/binary/color_code.png" class="slide" />
    </div>
  </div>

  <script>
    const slides = document.querySelectorAll('.slide');
    let index = 0;

    function updateSlides() {
      slides.forEach((slide, i) => {
        slide.classList.remove('active');
        if (i === index) {
          slide.classList.add('active');
        }
      });

      const track = document.querySelector('.carousel-track');
      const offset = (index * -220) + 190; // centers active
      track.style.transform = `translateX(${offset}px)`;
    }

    setInterval(() => {
      index = (index + 1) % slides.length;
      updateSlides();
    }, 3000);

    updateSlides();
  </script>

</body>
</html>

## Hands On Binary

This project is designed to teach binary in an engaging and interactive way using a hands-on 3D environment. Rather than relying on abstract concepts or traditional memorization, users will learn by directly manipulating objects that represent binary values. Whether it's flipping switches, stacking blocks, or activating machines, each action visually reinforces how binary works in computers. The goal is to make binary accessible to everyone—especially those who find the concept confusing at first but are curious and eager to understand how it powers the digital world around them.