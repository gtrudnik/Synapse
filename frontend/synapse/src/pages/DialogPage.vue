<script setup lang="ts">
import { ref } from 'vue';
import img2 from '../assets/img2.png'
import img3 from '../assets/img3.png'
import img4 from '../assets/img4.png'

interface Dialog {
  id: number;
  name: string;
  picture: any;
}

interface Message {
  id: number;
  dialogId: number;
  text: string;
  sender: string; // 'user' или 'user2'
}

const dialogs = ref<Dialog[]>([
  { id: 1, name: 'Илья', picture: img2 },
  { id: 2, name: 'Валерия', picture: img4 },
  { id: 3, name: 'Денис', picture: img3 },
]);

const messages = ref<Message[]>([
  { id: 1, dialogId: 1, text: 'Привет!', sender: 'user' },
  { id: 2, dialogId: 1, text: 'Здравствуйте!', sender: 'user2' },
  { id: 3, dialogId: 2, text: 'Как дела?', sender: 'user' },
  { id: 4, dialogId: 2, text: 'Все хорошо, спасибо!', sender: 'user2' },
  { id: 5, dialogId: 3, text: 'Что нового?', sender: 'user' },
  { id: 6, dialogId: 3, text: 'Ничего особенного.', sender: 'user2' },
  { id: 7, dialogId: 3, text: 'Но стоить отметить крайне интересную теорию вероятности!', sender: 'user2' },
  { id: 8, dialogId: 3, text: 'Каждое событие имеет шанс произойти 50%!', sender: 'user2' },
  { id: 9, dialogId: 3, text: 'Это почему?', sender: 'user' },
  { id: 10, dialogId: 3, text: 'Есть всего два варианта: событие происходит или нет. Значит шанс 50 на 50!', sender: 'user2' },
  { id: 11, dialogId: 3, text: 'Интересная гипотеза!', sender: 'user' },
]);

const selectedDialogId = ref<number | null>(null);

function selectDialog(id: number) {
  selectedDialogId.value = id;
}

function getMessagesForDialog() {
  if (selectedDialogId.value === null) return [];
  return messages.value.filter(msg => msg.dialogId === selectedDialogId.value);
}
</script>

<template>
  <div class="d-flex" style="height: 80vh;">
    <!-- Список диалогов -->
    <div class="border-end" style="width: 250px; overflow-y: auto;">
      <h5 class="p-3 mb-0">Диалоги</h5>
      <ul class="list-group list-group-flush">
        <li
          v-for="dialog in dialogs"
          :key="dialog.id"
          class="list-group-item list-group-item-action"
          :class="{ 'active': dialog.id === selectedDialogId }"
          @click="selectDialog(dialog.id)"
          style="cursor: pointer;"
        >
          <img
            :src="dialog.picture"
            class="dialog-image"
          />
          {{ dialog.name }}
        </li>
      </ul>
    </div>

    <!-- Чат -->
    <div class="flex-fill p-3" style="background: #f8f9fa; height: 100%; overflow-y: auto;">
      <h5 v-if="selectedDialogId">
        Диалог с {{ dialogs.find(d => d.id === selectedDialogId)?.name }}
      </h5>
      <p v-else>Выберите диалог</p>

      <div class="messages" style="max-height: calc(100vh - 150px); overflow-y: auto; padding-top: 10px;">
        <div v-for="msg in getMessagesForDialog()" :key="msg.id" class="d-flex mb-2" :class="{'justify-content-end': msg.sender==='user', 'justify-content-start': msg.sender==='user2'}">
          <div :class="{'bg-primary text-white p-2 rounded': msg.sender==='user',
                'bg-user2-message p-2 rounded': msg.sender==='user2'}">
            <img v-if="msg.sender==='user2'"
                :src="dialogs.find(d => d.id === selectedDialogId)?.picture"
                class="dialog-image"
              />
            {{ msg.text }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

.dialog-image {
  border-radius: 24px;
  width: 28px;
  height: 28px;
}

.bg-user2-message {
  background: #dbdbdb;
}

</style>