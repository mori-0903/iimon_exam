<template>
    <div>
      <div class="container">
        <input v-model="newItem" type="text">
        <button class="add-btn" @click="addItem">追加</button>
      </div>
      <ul>
        <li v-for="(item, index) in items" :key="index">
          <button class="delete-btn" @click="removeItem(index)">X</button>
            <!-- {{ item }} -->
          <span class="item">{{ item }}</span>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        items: [],
        newItem: ''
      };
    },
    methods: {
      addItem() {
        if (this.newItem.trim() !== '') {
          this.items.push(this.newItem.trim());
          this.newItem = '';
        }
      },
      removeItem(index) {
        this.items.splice(index, 1);
      }
    }
  };
  </script>

<style scoped>
.container {
  width: 300px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 50px;
}

input {
  flex: 1;
  height: 30px;
  border: 1px solid navy;
  padding: 0 5px;
  margin-right: 5px;
  box-sizing: border-box;
}

.add-btn {
  flex-shrink: 0;
  background-color: navy;
  color: white;
  border: none;
  padding: 0px 10px;
  cursor: pointer;
  height: 30px;
  display: flex;
  align-items: center;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 1px solid navy;
  box-sizing: border-box;
  padding: 0 10px;
  list-style-type: none;
  width: 300px;
  box-sizing: border-box;
  margin-bottom: 5px;
}

.delete-btn {
  background-color: navy;
  color: white;
  border: none;
  padding: 0;
  width: 50px;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  margin-left: -10px;
}

.item {
  flex: 1;
  text-indent: 20px;
}

body {
  font-size: 16px;
}
</style>
