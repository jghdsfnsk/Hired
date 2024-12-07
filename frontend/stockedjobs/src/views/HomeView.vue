<template>
  <div class="home">
    <section class="mb-10">
      <div class="flex flex-col items-center justify-center">
        <div class="bg-sky-950 text-center">
          <h1 class="text-6xl text-white font-bold">Welcome to Stocked Jobs</h1>
          <p class="text-xl mt-4">Get Your Dream Job here!</p>
        </div>
      </div>
    </section>
    <div class="container">
      <div class="text-center">
        <h1 class="text-4xl text-white font-bold">Top Jobs by Yearly Salary</h1>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-5 ml-20">
          <JobCard v-for="job in jobs" :key="job.id" :job="job"/>
        </div>
      </div>
    </div>
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
    return {
      jobs: []
    }
  },
  mounted(){
    this.getjobsbytopsalary()
    document.title = "Home | Stocked Jobs"
  },
  methods: {
    getjobsbytopsalary(){
      axios.get("/api/v1/top-salary-jobs/")
      .then(response => {
        this.jobs = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
  }
}
</script>