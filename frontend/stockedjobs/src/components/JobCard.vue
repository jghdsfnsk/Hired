<template>
  <div class="bg-gray-800 relative px-10 py-20">
    <div class="absolute top-0 left-0 bg-gray-800">
      <h3 class="text-white text-2xl">{{ job.title }}</h3>
      <p class="text-2m text-white">by {{ job.owner.username }}</p>
    </div>

    <div class="object-left absolute left-0">
      <p class="text-1l text-white">{{ job.summary }}</p>
    </div>

    <div class="absolute bottom-0 left-0">
      <router-link :to="job.get_absolute_url" class="text-white font-bold hover:underline">Details</router-link>
    </div>
    <div class="absolute bottom-0 right-0 ml-4"><p class="text-white">Yearly Salary: ${{ DisplaySalary(job.salary) }}</p></div>

  </div>
</template>






<script>
export default {
  name: "JobCard",
  props:["job"],
  methods: {
    DisplaySalary(salary) {
      return salary.toLocaleString();
    }
  }
}
</script> 