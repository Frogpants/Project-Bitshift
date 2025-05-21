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
    background-color: #1e3c72; /* initial blue */
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
    background-color: #8e24aa; /* final purple */
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
  }

  .circle:hover .text {
    color: #f3e5f5;
    text-shadow: 0 0 12px #ffffff, 0 0 25px #ce93d8;
  }
</style>

<div style="text-align: center;">
  <div class="circle">
    <div class="text">
      <p>Begin Experience</p>
    </div>
  </div>
</div>
