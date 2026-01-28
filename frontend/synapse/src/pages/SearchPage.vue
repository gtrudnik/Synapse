<script lang="ts" setup>
import { ref } from 'vue'
import { FlashCards } from 'vue3-flashcards'
import BasicCard from '../components/BasicCard.vue'

import img1 from '../assets/img1.png'
import img2 from '../assets/img2.png'

const cards = ref([
{
  id: 1,
  text: 'Паша',
  description: 'Я студент 1 курса магистратуры, мне нравится дисциплина машинное обучение. Хочу найти коллег для изучения данной дисциплины. Для меня будет удобно заниматься в вечернее время, днём на парах или на работе. ',
  image: img1,
},
{
  id: 2,
  text: 'Илья',
  description: 'Classic novels and poetry',
  image: img2
},
])

function handleSwipe(item: Card, direction: 'left' | 'right' | 'top') {
  console.log(2, item, direction)
}

</script>

<template>
  <div class="container d-flex align-items-center justify-content-between">
    <div>
      <i class="icon-no-active bi bi-x-circle-fill"></i>
    </div>

    <div>
      <FlashCards
        :items="cards"
        :swipe-direction="'horizontal'"
        @swipe-left="(item) => handleSwipe(item, 'left')"
        @swipe-right="(item) => handleSwipe(item, 'right')"
        #="{ item }"
      >
        <BasicCard
          :item="item"
        />
      </FlashCards>
      <!--
      <div class="actions">
          <button class="action-btn dislike" @click="left">
            👎
          </button>
          <button class="action-btn like" @click="right">
            ❤️
          </button>
      </div>
      -->
    </div>

    <div>
      <i class="icon-no-active bi bi-check-circle-fill"></i>
    </div>
  </div>
</template>

<style scoped>
.container {
  margin-top: 5vh;
  width: 100%;
}

.icon-no-active {
  color: #e3e3e3;
  font-size: 7rem;
}
</style>