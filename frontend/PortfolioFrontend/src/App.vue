<script setup>
import About from './components/About.vue';
import Education from './components/Education.vue';
import Work from './components/Work.vue';
import Projects from './components/Projects.vue';

// Import scroll animations script
import './scripts/scroll-animations.js';
</script>

<template>
  <div id="app">
    <img src="./pictures/longvine.png" alt="Vine Left" class="vine vine-side-left" />
    <img src="./pictures/longvine.png" alt="Vine Right" class="vine vine-side-right" />
    <img src="./pictures/flower2.png" alt="Bottom Left Vine" class="vine vine-bottom-left" />
    <img src="./pictures/flower2.png" alt="Bottom Right Vine" class="vine vine-bottom-right" />

    <main>
      <section id="about">
        <About />
      </section>
      <section id="education">
        <Education />
      </section>
      <section id="work">
        <Work />
      </section>
      <section id="projects">
        <Projects />
      </section>
    </main>
  </div>
</template>  

<style scoped>
@import './styles/vines.css';
</style>
