<template>
    <div id="all-products">
        <h1>Productos Disponibles</h1>

        <p><router-link :to="{ name: 'create_product' }" class="btn btn-primary">Crear Producto</router-link></p>

        <div class="form-group">
            <input type="text" name="search" v-model="productSearch" placeholder="Buscar..." class="form-control" v-on:keyup="searchProducts">
        </div>

        <table class="table table-hover">
            <thead>
            <tr>
                <td>Codigo</td>
                <td>Nombre</td>
                <td>Precio</td>
                <td>Disponibles</td>
                <td>Acciones</td>
            </tr>
            </thead>

            <tbody>
                <tr v-for="product in products">
                    <td>{{ product.codigo }}</td>
                    <td>{{ product.nombre }}</td>
                    <td>{{ product.precio }}</td>
                    <td>{{ product.exist }}</td>
                    <td>
                        <router-link :to="{name: 'edit_product', params: { product_id: product.id }}" class="btn btn-primary">Editar</router-link>
                        <router-link :to="{name: 'delete_product', params: { product_id: product.id }}" class="btn btn-danger">Borrar</router-link>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>

    export default{
        data(){
            return{
                products: [],
                originalProducts: [],
                productSearch: ''
            }
        },

        created: function()
        {
            this.fetchProductData();
        },

        methods: {
            fetchProductData: function()
            {
                this.$http.get('http://localhost:8098/api/products').then((response) => {
                    this.products = response.body;
                    this.originalProducts = this.products;
                }, (response) => {

                });
            },

            searchProducts: function()
            {
                if(this.productSearch == '')
                {
                    this.products = this.originalProducts;
                    return;
                }

                var searchedProducts = [];
                for(var i = 0; i < this.originalProducts.length; i++)
                {
                    var productName = this.originalProducts[i]['nombre'].toLowerCase();
                    if(productName.indexOf(this.productSearch.toLowerCase()) >= 0)
                    {
                        searchedProducts.push(this.originalProducts[i]);
                    }
                }

                this.products = searchedProducts;
            }
        }
    }
</script>
