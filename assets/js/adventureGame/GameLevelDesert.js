// To build GameLevels, each contains GameObjects from below imports
import GameEnv from './GameEnv.js';
import Background from './Background.js';
import PlayerOne from './PlayerOne.js';

import NpcTux from './NpcTux.js';


class GameLevelDesert {
  constructor(path) {
    const header = document.querySelector('header');
    const footer = document.querySelector('footer');

    // Values dependent on GameEnv.create()
    let width = GameEnv.innerWidth;
    let height = GameEnv.innerHeight;

    // Background data
    const image_src_desert = "https://github.com/user-attachments/assets/8e4e4e21-810f-405e-9a8d-9eb8c890d5a2";
    const image_data_desert = {
        name: 'water',
        src: image_src_desert,
        pixels: {height: 580, width: 1038}
    };

    // Player 1 sprite data (chillguy)
    const CHILLGUY_SCALE_FACTOR = 5;
    const sprite_src_chillguy = path + "/images/gamify/chillguy.png";
    const sprite_data_chillguy = {
        name: 'Chill Guy',
        src: sprite_src_chillguy,
        SCALE_FACTOR: CHILLGUY_SCALE_FACTOR,
        STEP_FACTOR: 1000,
        ANIMATION_RATE: 50,
        INIT_POSITION: { x: 0, y: height - (height/CHILLGUY_SCALE_FACTOR) }, 
        pixels: {height: 384, width: 512},
        orientation: {rows: 3, columns: 4 },
        down: {row: 0, start: 0, columns: 3 },
        left: {row: 2, start: 0, columns: 3 },
        right: {row: 1, start: 0, columns: 3 },
        up: {row: 3, start: 0, columns: 3 },
        hitbox: { widthPercentage: 0.45, heightPercentage: 0.2 },
    };



    // NPC sprite data (tux)
    const sprite_src_tux = path + "/images/gamify/tux.png";
    const sprite_data_tux = {
        name: 'npc',
        src: sprite_src_tux,
        SCALE_FACTOR: 10,  // Adjust this based on your scaling needs
        ANIMATION_RATE: 50,
        pixels: {height: 256, width: 352},
        INIT_POSITION: { x: (width / 2), y: (height / 2)},
        orientation: {rows: 8, columns: 11 },
        down: {row: 5, start: 0, columns: 3 },  // This is the stationary npc, down is default 
    };

    // List of objects defnitions for this level
    this.objects = [
      { class: Background, data: image_data_desert },
      { class: PlayerOne, data: sprite_data_chillguy },
      { class: NpcTux, data: sprite_data_tux }
    ];
  }

}

export default GameLevelDesert;