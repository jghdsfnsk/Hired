<template>
  <div class="about">
    <div class="text-center">
      <h1 class="text-white font-bold underline text-5xl uppercase">Ezekiel</h1>
      <p class="text-white text-3m">Sole developer of this website</p>
    </div>

    <figure>
      <img :src="require('@/assets/Profile.jpg')" alt="Ezekiel" class="rounded-full h-40 w-40 mx-auto" />
      <figcaption class="text-center text-white text-2m">"All for English Class" -Ezekiel</figcaption>
    </figure>
  </div>
</template>


<script>
export default {
  name: "AboutView",
  mounted(){
    document.title = "About | Stocked Jobs"
  }
}
</script>