<template>
    <div class="page-apply">
        <div class="text-center">
            <h1 class="text-white font-bold text-5xl uppercase">Apply</h1>
                <div class="mt-4">
                    <form @submit.prevent="Apply">
                    <div class="grid grid-cols-1 gap-10">
                        <div class="block ">
                            <label class="text-white mr-2 2m" for="Name">Username: </label>
                            <input type="text" v-model="username" class="mt-1 rounded-md bg-gray-100 border-transparent" id="Name">
                        </div>

                        <div class="block">
                            <label class="text-white mr-2 2m" for="desc">Why Should we hire you?: </label>
                        </div>

                        <div>
                            <textarea v-model="desc" rows="15" cols="200" class="mt-1 rounded-md bg-gray-100 border-transparent" id="desc"></textarea>
                        </div>

                        <div class="block">
                            <button class="bg-sky-700 py-2 px-5 rounded hover:bg-sky-800">Send Application</button>
                        </div>
                    </div>
                    </form>
                </div>

        </div>

    </div>
</template>




<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
    name: "JobApplyView",
    data() {
        return {
            username: "",
            desc: "",
            errors: []
        }
    },
    mounted(){
        document.title = "Application | Stocked Jobs"
    },
    methods: {
        Apply(){
            const username = this.$route.params.username
            const job_slug = this.$route.params.job_slug
            const csrfToken = Cookies.get('csrftoken')
            const formData = {
                username: this.username,
                desc: this.desc
            }
            axios.post(`/api/v1/${username}/${job_slug}/create/`, formData, {
                withCredentials: true,
                headers: {
                    'X-CSRFToken': csrfToken
                }
            })
            .then(response => {
                this.$router.push({name: "JobDetailView", params: {username: username, job_slug: job_slug}})
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