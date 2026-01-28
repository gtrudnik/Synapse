<script setup lang="ts">
import { ref } from 'vue'
import BasicCard from '../components/BasicCard.vue'
import img2 from '../assets/img2.png'

const item = ref({
  id: 2,
  text: 'Илья',
  description: 'Classic novels and poetry',
  image: img2
},);

</script>

<template>
  <div class="container-two-parts">
    <div class="left-block">
      <h2>Редактирование анкет</h2>
      <div style="margin-top: 5%; margin-right: 15%;">
          <div class="mb-3">
            <label for="subjectSelect" class="form-label">Выберите предмет</label>
            <select id="subjectSelect" class="form-select">
              <option value="" disabled selected>--- Выберите предмет ---</option>
              <option value="math">Математика</option>
              <option value="physics">Физика</option>
              <option value="chemistry">Химия</option>
              <option value="biology">Биология</option>
              <option value="literature">Литература</option>
              <option value="history">История</option>
            </select>
          </div>

          <!-- Многострочный текст для описания анкеты -->
          <div class="mb-3">
            <label for="descriptionTextarea" class="form-label">Описание анкеты</label>
            <textarea
              id="descriptionTextarea"
              class="form-control"
              rows="6"
              placeholder="Введите описание анкеты..."
            ></textarea>
          </div>

          <!-- Кнопка сохранить -->
          <button class="btn btn-primary w-100">Сохранить</button>
       </div>
    </div>
    <div class="right-block">
      <h2>Предпросмотр</h2>
      <BasicCard style="margin: auto; margin-top: 5%;" :item="item" />
    </div>
  </div>
</template>

<style scoped>
.container-two-parts {
  display: flex;
  width: 100vw;
  height: 90vh;
  margin: 0;
  padding: 0;
}

h2 {
  margin-top: 5px;
}

.left-block,
.right-block {
  flex: 1; /* Каждый блок занимает 50% ширины */
  height: 100%;
  display: flex;
  margin-left: 1%;
  display: block;
}

.left-block {
  border-right: 2px solid #ccc;
}

.right-block {

}


</style>
