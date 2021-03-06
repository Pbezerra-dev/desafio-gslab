import axios from 'axios'
import router from '../router'
import AuthService from './auth'
import ProductsService from './products'

const API_ENVS = {
  production: '',
  development: '',
  local: 'http://0.0.0.0:8000/api/v1'
}

const httpClient = axios.create({
  baseURL: API_ENVS.local
})

httpClient.interceptors.request.use(config => {
  const token = window.localStorage.getItem('token')

  if (token) {
    config.headers.common.Authorization = `Bearer ${token}`
  }

  return config
})

httpClient.interceptors.response.use((response) => response, (error) => {
  const canThrowAnError = error.request.status === 0 || error.request.status === 500

  if (canThrowAnError) {
    throw new Error(error.message)
  }

  if (error.response.status === 401) {
    router.push({
      name: 'Login'
    })
  }

  return error
})

export default {
  auth: AuthService(httpClient),
  products: ProductsService(httpClient)
}
