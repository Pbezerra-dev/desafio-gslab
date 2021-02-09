<template>
  <div class="home">
    <Navbar />

    <b-container>
      <Products />
    </b-container>

  </div>
</template>

<script>
import Products from '@/components/Products/Products'
import Navbar from '@/components/Navbar/Navbar'

export default {
  name: 'Home',
  components: {
    Products,
    Navbar
  }
}
</script>
