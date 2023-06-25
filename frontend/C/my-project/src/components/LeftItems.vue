<template>
    <div>
      <ul class="left-items">
        <li v-for="item in leftItems" :key="item">{{ item }}</li>
      </ul>
      <div class="button-container">
        <button @click="moveRight" class="move-btn">右へ移動</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    computed: {
      leftItems() {
        return this.$store.state.leftItems;
      },
    },
    methods: {
      moveRight() {
        this.$store.commit('MOVE_RIGHT');
      },
    },
  };
  </script>

<style scoped>

li {
  list-style:none;
}
.left-items {
  width: 300px;
  height: 600px;
  border: 1px solid navy;
  flex-direction: column;
  align-items: center;
  display: flex;
  list-style: none;
  margin-bottom: 0;
  box-sizing: border-box;
}
.left-items li {
  padding: 10px;
  border-bottom:1px solid navy;
  width: 80%;
  margin-bottom: 5px;
  text-align: center;
  margin-left: -40px;
}
.button-container {
  display: flex;
  justify-content: center;
}

.move-btn {
  height: 40px;
  width: 120px;
  background-color: navy;
  color: white;
  border: none;
  cursor: pointer;
  align-self: center;
  margin-top: 30px;
}
</style>