<template>
  <div class="main-container">
    <nav class="navbar navbar-expand-lg bg-body-tertiary nav-my-css">
      <div class="container-fluid">
        <RouterLink :to="{ name: 'movies' }" v-if="store.isLogin"
          >Home</RouterLink
        >
      </div>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item mx-2">
            <RouterLink :to="{ name: 'login' }" v-if="!store.isLogin"
              >Log in</RouterLink
            >
          </li>
          <li class="nav-item mx-2">
            <RouterLink :to="{ name: 'signup' }" v-if="!store.isLogin"
              >Sign Up</RouterLink
            >
          </li>
          <li class="nav-item mx-2"></li>
          <li class="nav-item dropdown" v-if="store.isLogin">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              안녕하세요! {{ store.logedinUsername }} 님!
            </a>
            <ul class="dropdown-menu" v-if="store.logedinUsername">
              <li>
                <RouterLink
                  :to="{
                    name: 'wishmovies',
                    params: { username: store.logedinUsername },
                  }"
                  class="dropdown-item"
                  >Wish Movie</RouterLink
                >
              </li>
              <li>
                <RouterLink
                  :to="{
                    name: 'mynotelist',
                    params: { username: store.logedinUsername },
                  }"
                  class="dropdown-item"
                  >Voca Note</RouterLink
                >
              </li>
              <li><hr class="dropdown-divider" /></li>
              <li>
                <RouterLink
                  :to="{
                    name: 'profile',
                    params: { username: store.logedinUsername },
                  }"
                  class="dropdown-item"
                  >My Page</RouterLink
                >
              </li>
              <li><hr class="dropdown-divider" /></li>
              <li><button @click="store.logOut">Log out</button></li>
            </ul>
          </li>
        </ul>
      </div>
    </nav>
    <RouterView />
    <chatBot />
    <footer>
      <div>
        <p>ⓒ 2024.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { useMovieStore } from "./stores/movie";
import chatBot from "./components/chatBot.vue";

const store = useMovieStore();
</script>

<style scoped></style>
