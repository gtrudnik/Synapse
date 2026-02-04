<template>
  <div class="d-flex justify-content-center align-items-center vh-100">
    <div class="card p-4 text-center" style="width: 350px;">
      <!-- Фото профиля -->
      <div class="d-flex justify-content-center">
        <img v-if="photoUrl" :src="photoUrl" class="ava mx-auto rounded-circle mb-3" alt="Фото профиля" />
        <div v-else class="d-flex justify-content-center align-items-center ava mx-auto mb-3 bg-secondary" style="width: 150px; height: 150px; border-radius: 50%;">
          <i class="bi bi-person" style="font-size: 3rem; color: #fff;"></i>
        </div>
      </div>

      <!-- Имя -->
      <h2>{{ name || 'Введите имя' }}</h2>

      <!-- Поле для имени -->
      <input
        v-model="name"
        type="text"
        class="form-control my-3"
        placeholder="Введите имя"
      />

      <!-- Кастомная кнопка для загрузки фото -->
      <button @click="triggerFileInput" class="btn btn-outline-primary mb-3">
        Загрузить фото
      </button>
      <!-- Скрытый input -->
      <input
        ref="fileInput"
        type="file"
        @change="loadPhoto"
        accept="image/*"
        style="display: none;"
      />

      <!-- Кнопка "Сохранить" -->
      <button class="btn btn-primary" @click="saveProfile">Сохранить</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const name = ref<string>('');
const photoUrl = ref<string | null>(null);
const fileInput = ref<HTMLInputElement | null>(null);

function triggerFileInput() {
  fileInput.value?.click();
}

function loadPhoto(event: Event) {
  const input = event.target as HTMLInputElement;
  if (input.files && input.files[0]) {
    const reader = new FileReader();
    reader.onload = () => {
      photoUrl.value = reader.result as string;
    };
    reader.readAsDataURL(input.files[0]);
  }
}

function saveProfile() {
  alert(`Сохранено!\nИмя: ${name.value}\nФото: ${photoUrl.value ? 'Загружено' : 'Не загружено'}`);
  // Здесь можете отправить данные на сервер или выполнить другую обработку
}
</script>


<style scoped>
.ava {
  margin: auto;
  width: 200px;
  height: 200px;
  object-fit: cover;
}
</style>
