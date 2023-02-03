<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <div class="container-fluid">
      <nav class="nav justify-content-between shadow">
        <RouterLink class="navbar-brand" to="/">
          <div class="d-flex align-items-center">
            <img
              alt="Vue logo"
              class="logo"
              src="@/assets/logo.svg"
              width="30"
              height="30"
            />
            <span>NTE MANAGEMENT DASHBOARD</span>
          </div>
        </RouterLink>
        <ul class="d-flex align-items-center m-0">
          <RouterLink class="nav-link" to="/">Home</RouterLink>
          <RouterLink class="nav-link" to="/input">Input NTE</RouterLink>
          <RouterLink class="nav-link" to="/odp">Input ODP</RouterLink>
        </ul>
      </nav>
      <footer class="mt-5">
        <div
          class="text-center bg-primary p-3 position-fixed bottom-0 start-50 translate-middle-x"
          style="width: 100%"
        >
          NTE Management Team @ 2023
        </div>
      </footer>
    </div>
    <!-- </div> -->
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1;
  max-height: 100vh;

  display: flex;
  place-items: center;
  padding-right: calc(var(--section-gap) / 2);
}

.logo {
  display: block;
  margin: 0 1rem 0 0;
}

nav {
  width: 100%;
  font-size: 1rem;
  text-align: center;
  padding: 1rem 1rem;
  margin-top: 0;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}
</style>
