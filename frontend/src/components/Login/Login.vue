<template>
  <div class="login col-md-4 offset-md-4">
    <h1 class="mb-2 text-center">Login</h1>
    <hr />
    <b-form @submit.prevent="onSubmit" @reset.prevent="onReset">
      <b-form-group id="input-group-1" label="Usuário" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="form.username"
          type="text"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Senha" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.password"
          type="password"
          autocomplete="on"
          required
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary" class="mr-2">Entrar</b-button>
      <b-button type="reset" variant="danger">Limpar</b-button>

      <div class="mt-3 mb-3" v-if="errors">
        <b-alert show variant="danger" class="text-center">
          {{ errors }}
        </b-alert>
      </div>
    </b-form>
  </div>
</template>

<script>
import service from '../../services'

export default {
  data () {
    return {
      form: {
        username: '',
        password: ''
      },
      errors: null
    }
  },
  methods: {
    async onSubmit () {
      try {
        const { data, errors } = await service.auth.login({
          username: this.form.username,
          password: this.form.password
        })

        if (!errors) {
          window.localStorage.setItem('token', data.access)
          this.$router.push({ name: 'Home' })
          return
        }

        if (errors.status === 404) {
          this.errors = 'Email não encontrado'
        }
        if (errors.status === 401) {
          this.errors = 'Email ou senha inválidos'
        }
        if (errors.status === 400) {
          this.errors = 'Ocorreu um erro ao fazer o login'
        }
      } catch (error) {
        this.errors = 'Ocorreu um erro ao fazer o login'
      }
    },
    onReset () {
      this.form.username = ''
      this.form.password = ''
    }
  }
}
</script>

<style scoped>
.login {
  margin-top: 25%;
}
</style>
