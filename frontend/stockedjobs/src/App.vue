<template>
  <div id="wrapper">
    <Disclosure as="nav" class="bg-gray-800" v-slot="{ open }">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="relative flex h-16 items-center justify-between">
        <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
          <div class="flex shrink-0 items-center">
            <img class="h-8 w-auto" src="https://tailwindui.com/plus/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company" />
          </div>
          <div class="hidden sm:ml-6 sm:block">
            <div class="flex space-x-4">
              <router-link to="/" class=" text-white px-3 py-2 rounded-md text-sm font-medium" aria-current="page">Home</router-link>
              <router-link to="/about" class="text-white px-3 py-2 rounded-md text-sm font-medium" aria-current="page">About</router-link>
              <router-link to="/jobs" class="text-white px-3 py-2 rounded-md text-sm font-medium" aria-current="page">Jobs</router-link>
            </div>
          </div>
        </div>
        <div class="absolute inset-y-0 right-0 flex items-center">
          <div class="p-11">
            <button type="button" class="text-amber-50 px-10 py-4 text-2xl bg-gray-850 hover:bg-sky-950 active:bg-sky-500 "><router-link to="/log-in" aria-current="page">Login</router-link></button>
          </div>
          <div class="p-11">
          <button type="button" class="text-amber-50 bg-gray-850 ml-3 px-10 py-4 text-2xl hover:bg-sky-950 active:bg-sky-500 ">Applications</button>
          </div>
          
        </div>
      </div>
    </div>
  </Disclosure>
  
  <section class="bg-indigo-950 min-h-screen">
      <router-view/>
    </section>
  
  <footer>
    <p class="text-center bg-indigo-950 text-white text-3m">Copyright (c) 2024</p>
  </footer>
  </div>
  
</template>

<script setup>
import { Disclosure} from '@headlessui/vue'
</script>

<script>
import axios from 'axios'
export default {
  beforeCreate() {
    this.$store.commit("getUserState")
    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token" + token
    } else {
      axios.defaults.headers.common["Authorization"] = ''
    }
  }
}
</script>