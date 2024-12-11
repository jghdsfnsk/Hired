<template>
    <div class="page-log-in">
        <div class="text-center">
            <h1 class="text-white font-bold text-5xl uppercase">Log in</h1>
                <div class="mt-4">
                    <form @submit.prevent="submitForm">
                    <div class="grid grid-cols-1 gap-10">
                        <div class="block ">
                            <label class="text-white mr-2 2m" for="Name">Username: </label>
                            <input type="text" v-model="username" class="mt-1 rounded-md bg-gray-100 border-transparent" id="Name">
                        </div>

                        <div class="block">
                            <label class="text-white mr-2 2m" for="password">Password: </label>
                            <input type="password" v-model="password" class="mt-1 rounded-md bg-gray-100 border-transparent " id="password">
                        </div>

                        <div class="block">
                            <button class="bg-sky-700 py-2 px-5 rounded hover:bg-sky-800">Login</button>
                            <p class="text-sm text-white mt-3">OR <router-link to="/sign-up" class="font-bold text-m text-white hover:underline" aria-current="page">Make an account</router-link></p>
                        </div>
                    </div>
                    </form>
                </div>

        </div>

    </div>
</template>





<script>
import axios from 'axios'

export default {
    name: "LoginView",
    data() {
        return {
            username: "",
            password: "",
            errors: []
        }
    },
    mounted(){
        document.title = "Log In | Stocked Jobs"
    },
    methods: {
        submitForm(){
            axios.defaults.headers.common["Authorization"] = ''

            localStorage.removeItem("token")
            this.$store.commit("removeToken")

            const formData = {
                username: this.username,
                password: this.password
            }

            axios.post("/api/v1/token/login/", formData)
            .then(response => {
                const token = response.data.auth_token

                this.$store.commit("setToken", token)
                
                axios.defaults.headers.common["Authorization"] = "Token " + token

                localStorage.setItem("token", token)

                const toPath = this.$route.query.to || "/jobs"
                this.$router.push(toPath)
            })
            .catch(error => {
                if (error.response){
                    for (const property in error.response.data){
                        this.errors.push(`${property}: ${error.response.data[property]}`)
                    }
                } else {
                    this.errors.push('Something went wrong. Please try again')
                    console.log(JSON.stringify(error))
                }
            })
        }
    }
}
</script>