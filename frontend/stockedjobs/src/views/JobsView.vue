<template>
    <div class="jobs">
        <div class="text-center">
            <h1 class="text-white font-bold underline ">All Jobs</h1>
        </div>

        <div class="container">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-5 ml-20">
            <JobCard v-for="job in jobs" :key="job.id" :job="job"/>
            </div>
        </div>
    </div>
  </template>
  
  
<script>
import JobCard from '@/components/JobCard.vue'
import axios from 'axios'
export default {
    name: "JobsView",
    mounted(){
        this.getJobs()
        document.title = "Jobs | Stocked Jobs"
    },
    components: {
    JobCard
    },
    data() {
        return {
        jobs: []
        }
    },
    methods: {
        getJobs(){
            axios.get("/api/v1/all-jobs/")
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