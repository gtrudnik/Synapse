<script setup lang="ts">
import { ref } from 'vue'
import logo from '../assets/synapse.png';

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
      <img :src="logo" alt="Logo" class="navbar-nav me-auto mb-2 mb-lg-0" style="width: 24px; height: auto;" />
      <!-- Навигационные ссылки -->
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <router-link class="nav-link" to="/search">Поиск друга</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/form">Анкеты</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/match">Мэтчи</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/dialog">Диалоги</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/profile">Профиль</router-link>
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

