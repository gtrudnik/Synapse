<script setup lang="ts">
import { ref } from 'vue'

const isAuthenticated = ref(true)

// Функция выхода
function logout() {
  alert('Вы вышли из аккаунта')
  isAuthenticated.value = false
}
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light px-3 py-2 shadow-sm">
    <div class="container-fluid">
      <!-- Навигационные ссылки -->
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <router-link class="nav-link" to="/">Главная</router-link>
        </li>
        <li class="nav-item" v-if="isAuthenticated">
          <router-link class="nav-link" to="/profile">Профиль</router-link>
        </li>
        <li class="nav-item" v-if="!isAuthenticated">
          <router-link class="nav-link" to="/login">Войти</router-link>
        </li>
        <li class="nav-item" v-if="!isAuthenticated">
          <router-link class="nav-link" to="/register">Регистрация</router-link>
        </li>
      </ul>

      <!-- Кнопка выхода с иконкой -->
      <button
        v-if="isAuthenticated"
        class="btn"
        @click="logout"
        title="Выйти"
      >
        <i class="bi bi-box-arrow-right"></i>
      </button>
    </div>
  </nav>
</template>

