<template>
  <div class="container">
    <div class="centered-container">
      <LeftItems />
      <RightItems />
    </div>
  </div>
</template>

<script>
import LeftItems from './components/LeftItems.vue';
import RightItems from './components/RightItems.vue';

export default {
  components: {
    LeftItems,
    RightItems,
  },
};
</script>

<style>
.container {
  display: flex;
  justify-content: center;
  font-size: 16px;
}

.centered-container {
  width: 700px;
  display: flex;
  justify-content: space-between;
}
</style>
