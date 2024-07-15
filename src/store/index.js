// store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    message: 'Hello Vuex'
  },
  mutations: {
    setMessage(state, message) {
      state.message = message;
    }
  },
  actions: {
    updateMessage({ commit }, message) {
      commit('setMessage', message);
    }
  },
  modules: {}
});
