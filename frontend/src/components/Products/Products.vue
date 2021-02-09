<template>
  <div class=" mt-5">
    <h2 class="text-center text-uppercase">
      Lista de Produtos |
      <b-button class="btn-sm" variant="info" v-b-modal.modal-product
        >Adicionar Produto</b-button
      >
    </h2>
    <hr class="w-50" />

    <!-- Add and Update Product -->
    <div>
      <b-modal
        id="modal-product"
        ref="modal"
        title="Adicionar produtos"
        centered
        @show="resetModal"
        @hidden="resetModal"
        @ok="handleOk"
      >
        <form ref="form" @submit.prevent="handleSubmit">
          <b-form-group
            label="Nome"
            label-for="name-input"
            invalid-feedback="Campo obrigatório"
          >
            <b-form-input
              id="name-input"
              v-model="form.name"
              required
              :state="nameState"
            ></b-form-input>
          </b-form-group>
          <b-form-group
            label="Descrição"
            label-for="description-input"
            invalid-feedback="Campo obrigatório"
          >
            <b-form-textarea
              id="description-input"
              v-model="form.description"
              :state="descriptionState"
              required
            ></b-form-textarea>
          </b-form-group>
          <b-form-group
            label="Preço"
            label-for="price-input"
            invalid-feedback="Campo obrigatório"
          >
            <b-form-input
              id="price-input"
              v-model="form.price"
              type="number"
              :state="priceState"
              required
            >
              </b-form-input>
          </b-form-group>
        </form>
      </b-modal>
    </div>

    <!-- Delete Product -->
    <b-modal id="delete-product" centered @ok="excludeProduct(id_prod)"
      >Tem certeza que deseja <strong class="text-danger">excluir</strong> o
      produto?</b-modal
    >

    <b-table striped hover :items="items" :fields="fields" responsive="sm">
      <template v-slot:cell(actions)="{ item }">
        <b-button
          class="btn-sm"
          variant="warning"
          v-b-modal.modal-product
          @click="getProductsById(item.id)"
        >
          editar
        </b-button>

        <b-button
          class="ml-2 btn-sm"
          variant="danger"
          v-b-modal.delete-product
          @click="setId(item.id)"
        >
          excluir
        </b-button>
      </template>
    </b-table>
  </div>
</template>

<script>
import service from '../../services'
import { formatCurrency } from '../../utils/formatters'

export default {
  data () {
    return {

      form: {
        name: '',
        description: '',
        image: ''
      },
      nameState: null,
      descriptionState: null,
      priceState: null,
      update: false,
      id_prod: 0,
      items: [],
      fields: [
        { key: 'name', label: 'Nome' },
        { key: 'description', label: 'Descrição' },
        {
          key: 'price',
          label: 'Preço',
          formatter: value => formatCurrency(value)
        },
        { key: 'actions', label: 'Ações', class: 'text-center' }
      ]
    }
  },
  created () {
    this.handleProducts()
  },
  methods: {
    async handleProducts () {
      const products = await service.products.getProducts()
      this.items = products.data
    },

    async getProductsById (prodId) {
      this.update = true
      this.setId(prodId)
      await service.products.getProductById(prodId).then(resp => {
        this.form.name = resp.data.name
        this.form.description = resp.data.description
        this.form.price = resp.data.price
      })
    },
    checkFormValidity () {
      const valid = this.$refs.form.checkValidity()
      this.nameState = valid
      this.descriptionState = valid
      this.priceState = valid
      return valid
    },
    resetModal () {
      this.form.name = ''
      this.form.description = ''
      this.form.price = ''
      this.nameState = null
      this.descriptionState = null
      this.priceState = null
    },
    handleOk (bvModalEvt) {
      bvModalEvt.preventDefault()

      if (!this.update) {
        this.AddProductSubmit()
      } else {
        this.updateProductSubmit()
      }
    },
    setId (id) {
      this.id_prod = id
    },
    async excludeProduct (prodId) {
      await service.products.deleteProduct(prodId)
      location.reload()
    },
    async AddProductSubmit () {
      if (!this.checkFormValidity()) {
        return
      }
      await service.products
        .addProducts(this.form)
        .then(location.reload())
        .catch(err => console.log(err))
    },
    async updateProductSubmit () {
      await service.products.updateProduct(this.id_prod, this.form)
        .then(location.reload())
    }
  }
}
</script>

<style scoped>
.home {
  margin-top: 10%;
}
hr {
  margin-bottom: 8%;
}
</style>
