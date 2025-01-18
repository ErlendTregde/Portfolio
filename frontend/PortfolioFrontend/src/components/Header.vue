<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <header>
    <div class="logo-wrapper">
      <img class="logo" src="@/assets/logo.svg" alt="Logo" />
    </div>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About Me</RouterLink>
      <RouterLink to="/projects">Projects</RouterLink>
    </nav>
  </header>
</template>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #1e1e2c; /* Dark background */
  color: #fff; /* Light text */
}

.logo-wrapper {
  display: flex;
  align-items: center;
}

.logo {
  height: 50px;
  margin-right: 15px;
}

nav {
  display: flex;
  gap: 15px;
}

nav a {
  text-decoration: none;
  color: #fff;
  font-weight: bold;
  padding: 5px 10px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

nav a:hover {
  background-color: #00ffff; /* Highlight hover effect */
  color: #1e1e2c;
}
</style>
