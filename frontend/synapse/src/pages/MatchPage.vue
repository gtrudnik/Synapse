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
  description: 'Physics and chemistry fundamentals',
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
  <h3 class="text-center">Хочет с Вами учить математику</h3>
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
.text-center {
  text-align: center;
  margin-top: 2vh;
}

.container {
  margin-top: 3vh;
  width: 100%;
}

.icon-no-active {
  color: #e3e3e3;
  font-size: 7rem;
}
</style>