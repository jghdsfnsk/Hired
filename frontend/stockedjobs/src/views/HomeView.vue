<template>
  <div class="home">
    <h1>This is the home page</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import JobCard from '@/components/JobCard.vue'
import axios from 'axios'
export default {
  name: 'HomeView',
  components: {
    JobCard
  },
  data() {
    return {}
  },
  mounted(){
    document.title = "Home | Stocked Jobs"
  }
}
</script>