import { createStore } from 'vuex'

export default createStore({
  state: {
    navigation: [
      { name: 'Home', href: '/', current: true },
      { name: 'About', href: '/about', current: false },
      { name: 'Jobs', href: '/jobs', current: false }
    ],
    isAuthenticated: false,
    token: ''
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
