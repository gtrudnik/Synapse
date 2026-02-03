import { defineStore } from "pinia";
import { ref } from 'vue'
import { apiClient } from "../utils/axios";

export const useAuth = defineStore('auth', () => {
  const isAuthenticated = ref(false)

  async function login(login: string, password: string) {
    const response = await apiClient.post("/auth/login", new URLSearchParams({
        username: login,
        password: password,}),
    )
    isAuthenticated.value = true
  }

  async function logout() {
    isAuthenticated.value = false
  }

  return {
    isAuthenticated,
    login,
    logout
  }
})