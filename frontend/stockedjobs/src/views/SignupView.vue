<template>
    <div class="page-sign-up">
        <div class="text-center">
            <h1 class="text-white font-bold text-5xl uppercase">Sign up</h1>
                <div class="mt-4">
                    <form @submit.prevent="submitForm">
                    <div class="grid grid-cols-1 gap-10">
                        <div class="block">
                            <label class="text-white mr-2 2m" for="Name">Username: </label>
                            <input type="text" v-model="username" class="mt-1 rounded-md bg-gray-100 border-transparent" id="Name">
                        </div>

                        <div class="block">
                            <label class="text-white mr-2 2m" for="password">Password: </label>
                            <input type="password" v-model="password" class="mt-1 rounded-md bg-gray-100 border-transparent " id="password">
                        </div>

                        <div class="block">
                            <label class="text-white mr-2 2m" for="password2">Confirm Password: </label>
                            <input type="password" v-model="password2" class="mt-1 rounded-md bg-gray-100 border-transparent " id="password2">
                        </div>

                        <div class="block">
                            <label class="text-white mr-2 2m" for="email">Email Address: </label>
                            <input type="email" v-model="email" class="mt-1 rounded-md bg-gray-100 border-transparent " id="email">
                        </div>

                        <div class="block">
                            <button class="bg-sky-700 py-2 px-5 rounded hover:bg-sky-800">Sign up</button>
                            <p class="text-sm text-white mt-3">OR <router-link to="/log-in" class="font-bold text-m text-white hover:underline" aria-current="page">Use an existing account</router-link></p>
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
    name: "SignUpView",
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            email: '',
            errors: []
        }
    },
    mounted(){
        document.title = "Sign Up | Stocked Jobs"
    },
    methods: {
        submitForm(){
            this.errors = []
            if(this.username === ''){
                this.errors.push('Username is required')
            }
            if(this.password === ''){
                this.errors.push('Password is required')
            }
            if(this.email === ''){
                this.errors.push('Email is required')
            }
            if(this.password !== this.password2){
                this.errors.push('Passwords do not match')
            }
            if(this.errors.length === 0){
                const formData = {
                    username: this.username,
                    password: this.password,
                    email: this.email
                }
                axios.post('/api/v1/users/',formData)
                .then(response => {
                    this.$router.push('/log-in')
                }).catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('An error occurred. Please try again.')
                    }
                })
            }
        }
    }
}
</script>