<script setup lang="ts">
import { ref } from 'vue';
import logo from '../assets/synapse.png';
import { apiClient } from "../utils/axios";

const email = ref('');
const login = ref('');
const password = ref('');
const password_repeat = ref('');

async function Register() {
  if (password_repeat.value != password.value) {
    alert(`Пароли не совпадают `);
  } else {
    const response = await apiClient.post("/auth/login", {
        email: email.value,
        username: login.value,
        password: password.value,
      }
    )
  }
}

</script>

<template>
  <div class="d-flex justify-content-center align-items-center" style="margin-top: 10vh">
    <div class="card p-4" style="width: 100%; max-width: 450px; max-height: 70vh;">
      <img :src="logo" alt="Logo" class="mb-3" style="width: 100px; height: auto; margin: 0 auto;" />
      <h1 class="text-center mb-4">Synapse</h1>
      <form @submit.prevent="Register">
        <div class="mb-3">
          <label for="email" class="form-label">Почта</label>
          <input
            v-model="email"
            type="text"
            class="form-control"
            id="email"
            placeholder="Введите логин"
            required
          />
        </div>
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
        <div class="mb-3">
          <label for="password" class="form-label">Подтверждение пароля</label>
          <input
            v-model="password_repeat"
            type="password"
            class="form-control"
            id="password_repeat"
            placeholder="Повторите пароль"
            required
          />
        </div>
        <div class="d-flex gap-3">
          <button type="submit" class="btn btn-primary w-100">Зарегистрироваться</button>
        </div>
        <div class="d-flex justify-content-center">
          <p class="mt-2 mb-0 text-center">
            Уже есть аккаунт? <a href="/">Войти в аккаунт</a>
          </p>
        </div>
      </form>
    </div>
  </div>
</template>

