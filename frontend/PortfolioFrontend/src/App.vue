<script setup>
import { ref, onMounted } from 'vue';
import About from './components/About.vue';
import Education from './components/Education.vue';
import Work from './components/Work.vue';
import Projects from './components/Projects.vue';

import './scripts/scroll-animations.js';

const isMobile = ref(false);

const checkIfMobile = () => {
  isMobile.value = window.innerWidth <= 768;
};

onMounted(() => {
  checkIfMobile();
  window.addEventListener('resize', checkIfMobile);
});
</script>


<template>
  <div id="app">
    <img v-if="!isMobile" src="./pictures/longvine.png" alt="Vine Left" class="vine vine-side-left" />
    <img v-if="!isMobile" src="./pictures/longvine.png" alt="Vine Right" class="vine vine-side-right" />
    <img v-if="!isMobile" src="./pictures/flower2.png" alt="Bottom Left Vine" class="vine vine-bottom-left" />
    <img v-if="!isMobile" src="./pictures/flower2.png" alt="Bottom Right Vine" class="vine vine-bottom-right" />

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
        <Projects :isMobile="isMobile" />
      </section>
    </main>
  </div>
</template>

<style scoped>
@import './styles/vines.css';
</style>


<style scoped>
@import './styles/vines.css';
</style>
