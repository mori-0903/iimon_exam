import { createApp } from 'vue';
import App from './App.vue';
import store from './store/store.js';

const app = createApp(App);
app.use(store); // storeプラグインをアプリケーションに使用する

app.mount('#app');
