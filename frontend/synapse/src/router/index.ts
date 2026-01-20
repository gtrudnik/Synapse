// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router'

// Импортируйте компоненты страниц
import AuthPage from '../pages/AuthPage.vue'
import RegisterPage from '../pages/RegisterPage.vue'

const routes = [
  { path: '/', component: AuthPage },
  { path: '/register', component: RegisterPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router