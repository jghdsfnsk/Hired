<template>
    <div class="page-job-details">
        <div class="text-center">
            <h1 class="text-white text-6xl underline font-bold uppercase mb-4">{{ job.title }}</h1>
            <h2 class="text-white font-bold text-3l mb-4">Yearly Salary: ${{ job.salary }}</h2>
            <h2 class="text-white font-bold text-3l mb-4">{{ job.city }} in {{ job.state }}</h2>
        </div>

        <div class="text-center">
            <h2 class="text-white font-bold text-3l mb-4">Description: </h2>
            <p class="text-white text-lg">{{ job.fulldescription }}</p>

            <button class="bg-sky-700 py-2 px-5 rounded hover:bg-sky-800"><router-link :to="applyLink" class="font-bold text-white" aria-current="page">Apply</router-link></button>
        </div>
    </div>
</template>





<script>
import axios from 'axios'
export default {
    name: "JobDetailView",
    data() {
        return {
            job: {},
            errors: [],
            applyLink:""
        }
    },
    mounted(){
        this.getJob()
    },
    methods: {
        getJob(){
            const username = this.$route.params.username
            const job_slug = this.$route.params.job_slug
            this.applyLink = `/${username}/${job_slug}/apply`
            axios.get(`/api/v1/${username}/${job_slug}`)
            .then(response => {
                this.job = response.data
                document.title = `${this.job.title} | Stocked Jobs`
            })
            .catch(error => {
                if (error.response){
                    for (const property in error.response.data){
                        this.errors.push(`${property}: ${error.response.data[property]}`)
                    }
                } else {
                    this.errors.push('An error occurred. Please try again.')
                }
            })
        }
    }
}
</script>