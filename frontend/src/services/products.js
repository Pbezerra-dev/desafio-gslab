export default httpClient => ({
  getProducts: async () => {
    const response = await httpClient.get('/products')

    return {
      data: response.data
    }
  },
  getProductById: async (prodID) => {
    const response = await httpClient.get(`/products/${prodID}`)

    return {
      data: response.data
    }
  },
  addProducts: async (form) => {
    const response = await httpClient.post('/products', { ...form })

    return {
      data: response.data
    }
  },
  deleteProduct: async (prodID) => {
    const response = await httpClient.delete(`/products/${prodID}/delete`)

    return {
      data: response.data
    }
  },
  updateProduct: async (prodID, form) => {
    const response = await httpClient.put(`/products/${prodID}/update`, { ...form })

    return {
      data: response.data
    }
  }
})
