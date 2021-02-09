export default httpClient => ({
  login: async ({
    username,
    password
  }) => {
    const response = await httpClient.post('/login', {
      username,
      password
    })
    let errors = null

    if (!response.data) {
      errors = {
        status: response.request.status,
        statusText: response.request.statusText
      }
    }

    return {
      data: response.data,
      errors
    }
  }
})
