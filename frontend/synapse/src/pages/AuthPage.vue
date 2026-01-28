<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router'
import logo from '../assets/synapse.png';

const router = useRouter()

const login = ref('');
const password = ref('');

function onLogin() {
  alert(`Логин: ${login.value}, Пароль: ${password.value}`);
}

function onRegister() {
  router.push('/register')
}
</script>

<template>
  <div class="d-flex justify-content-center align-items-center" style="margin-top: 20vh">
    <div class="card p-4" style="width: 100%; max-width: 400px;">
      <img :src="logo" alt="Logo" class="mb-3" style="width: 100px; height: auto; margin: 0 auto;" />
      <h1 class="text-center mb-4">Synapse</h1>
      <form @submit.prevent="onLogin">
        <div class="mb-3">
          <label for="login" class="form-label">Логин</label>
          <input
            v-model="login"
            type="text"
            class="form-control"
            id="login"
            placeholder="Введите логин"
            required
          />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Пароль</label>
          <input
            v-model="password"
            type="password"
            class="form-control"
            id="password"
            placeholder="Введите пароль"
            required
          />
        </div>
        <div class="d-flex gap-3">
          <button type="submit" class="btn btn-primary w-50">Войти</button>
          <button type="button" class="btn btn-secondary w-50" @click="onRegister">
            Зарегистрироваться
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

