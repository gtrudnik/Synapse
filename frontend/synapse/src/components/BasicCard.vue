<script setup lang="ts">
interface TinderItem {
  id: number
  text: string
  description: string
  image: string
}

defineProps<{
  item: TinderItem,
  left?: () => void
  right?: () => void
}>()
</script>

<template>
  <div class="card">
    <img
      :src="item.image"
      :alt="item.text"
      class="card-image"
    />
    <div class="text-part">
      <h2 class="">
        {{ item.text }}
      </h2>
      <p class="m-0 text-base drop-shadow-md">
        {{ item.description }}
      </p>
    </div>
  </div>
</template>

<style>
.card {
  margin: auto;
  width: 30vw;
  height: 80vh;
  background: #ededed;

  border: 4px solid transparent;
  border-radius: 15px;
  background-clip: border-box;
  position: relative;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.card-image {
  max-width: 95%;           /* Занимает 95% ширины родителя */
  height: 65%;         /* Сохраняет пропорции */
  display: block;       /* Убирает пробел под изображением (важно!) */
  margin: 0 auto;       /* Центрирует по горизонтали — равномерные отступы слева/справа */
  margin-top: 2%;
  border-radius: 8px;   /* Опционально: закруглённые углы */
  object-fit: cover;    /* Опционально: если нужно обрезать по размеру, а не растягивать */
  pointer-events: none;
}


.actions {
  position: absolute;
  bottom: 1rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 2rem;
  z-index: 3;
  pointer-events: auto;
}

.action-btn {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.action-btn:hover {
  transform: scale(1.1);
}

.action-btn:active {
  transform: scale(0.95);
}

.like {
  color: #e74c3c; /* красный */
}

.dislike {
  color: #3498db; /* синий */
}

/* Дополнительно: при нажатии — визуальный эффект */
.like:active {
  background-color: #e74c3c;
  color: white;
}

.dislike:active {
  background-color: #3498db;
  color: white;
}

.text-part {
  margin-left: 10px;
}
</style>