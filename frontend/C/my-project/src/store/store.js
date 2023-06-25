import { createStore } from 'vuex';

export default createStore({
  state() {
    return {
      leftItems: ['Apple', 'Grape', 'Strawberry', 'Cherry', 'Plum'],
      rightItems: ['Watermelon', 'Banana', 'Peach'],
    };
  },
  mutations: {
    MOVE_LEFT(state) {
      if (state.rightItems.length > 0) {
        const item = state.rightItems.pop();
        state.leftItems.push(item);
      }
    },
    MOVE_RIGHT(state) {
      if (state.leftItems.length > 0) {
        const item = state.leftItems.pop();
        state.rightItems.push(item);
      }
    },
  },
});
