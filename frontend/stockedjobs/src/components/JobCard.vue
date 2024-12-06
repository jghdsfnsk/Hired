<template>
  <div class="bg-grey-750 relative">
    <div class="absolute top-0 right-0">
      <h3 class="mb-4 text-white">{{ job.title }}</h3>
      <p class="mb-4">{{ job.owner.username }}</p>
    </div>

    <div class="absolute bottom-0 left-0">
      <button>Apply</button>
    </div>
  </div>
</template>






<script>
export default {
  name: "JobCard",
  props:["job"]
}
</script> 