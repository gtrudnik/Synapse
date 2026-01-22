// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router'

// Импортируйте компоненты страниц
import AuthPage from '../pages/AuthPage.vue'
import RegisterPage from '../pages/RegisterPage.vue'
import SearchPage from '../pages/SearchPage.vue'
import FormPage from '../pages/FormPage.vue'
import MatchPage from '../pages/MatchPage.vue'
import DialogPage from '../pages/DialogPage.vue'
import ProfilePage from '../pages/ProfilePage.vue'

const routes = [
  { path: '/', component: AuthPage },
  { path: '/register', component: RegisterPage },
  { path: '/search', component: SearchPage },
  { path: '/form', component: FormPage },
  { path: '/match', component: MatchPage },
  { path: '/dialog', component: DialogPage },
  { path: '/profile', component: DialogPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router