<template>
  <div>
    <Navbar />
    <Slider />
    <div class="container">
      <Nuxt />
    </div>
    <Footer />
  </div>
</template>


<script>
import Navbar from "~/components/Navbar";
import Slider from "~/components/Slider";
import Footer from "@/components/Footer";

export default {
  components: {
    Footer,
    Slider,
    Navbar,
  }
};
</script>

<style>

</style>