<template>
  <b-container>
    <div class="login">
      <login />
    </div>
  </b-container>
</template>

<script>
import Login from '@/components/Login/Login.vue'

export default {
  name: 'LoginView',
  components: {
    Login
  }
}
</script>
