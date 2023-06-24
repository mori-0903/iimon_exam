<template>
  <div id="app">
    <item-list></item-list>
  </div>
</template>

<script>
import ItemList from './components/ItemList.vue';

export default {
  components: {
    ItemList
  }
};
</script>

<style>
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>