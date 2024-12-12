<template>
</template>





<script>
import axios from 'axios'
export default {
    name: "JobDetailView",
    data() {
        return {
            job: {},
            errors: []
        }
    },
    mounted(){
        document.title = "Job Detail | Stocked Jobs"
        this.getJob()
    },
    methods: {
        getJob(){
            const jobId = this.$route.params.id
            axios.get(`/api/v1/jobs/${jobId}`)
            .then(response => {
                this.job = response.data
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