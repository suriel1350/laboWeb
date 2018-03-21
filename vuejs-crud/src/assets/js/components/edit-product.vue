<template>
    <div id="update-product">
        <h1>Editar Producto</h1>

        <p><router-link :to="{ name: 'all_products' }">Volver al menú</router-link></p>

        <notification v-bind:notifications="notifications"></notification>

        <form v-on:submit.prevent="editProduct">
            <div class="form-group">
                <label name="product_codigo">Codigo</label>
                <input type="number" class="form-control" v-model="product.codigo" id="product_codigo" required>
            </div>

            <div class="form-group">
                <label name="product_nombre">Nombre</label>
                <input type="text" class="form-control" v-model="product.nombre" id="product_nombre" required>
            </div>

            <div class="form-group">
                <label name="product_precio">Precio</label>
                <input type="text" class="form-control" v-model="product.precio" id="product_precio" required>
            </div>

            <div class="form-group">
                <label name="product_exist">Disponibles</label>
                <input type="text" class="form-control" v-model="product.exist" id="product_exist" required>
            </div>

            <div class="form-group">
                <button class="btn btn-primary">Update</button>
            </div>
        </form>
    </div>
</template>

<script>
    import Notification from './notifications.vue';

    export default{
        data(){
            return{
                product:{},
                notifications:[]
            }
        },

        created: function(){
            this.getProduct();
        },

        methods: {
            getProduct: function()
            {
                this.$http.get('http://localhost:8098/api/products/' + this.$route.params.product_id).then((response) => {
                    this.product = response.body;
                }, (response) => {

                });
            },

            editProduct: function()
            {
                // Validation
                var price = parseFloat(this.product.precio);
                if(isNaN(price))
                {
                    this.notifications.push({
                        type: 'danger',
                        message: 'Precio debe ser un numero'
                    });
                    return false;
                }

                this.$http.put('http://localhost:8098/api/products/' + this.$route.params.product_id, this.product, {
                    headers : {
                        'Content-Type' : 'application/json'
                    }
                }).then((response) => {
                    this.notifications.push({
                        type: 'success',
                        message: 'Product actualizado satisfactoriamente'
                    });
                }, (response) => {
                    this.notifications.push({
                        type: 'error',
                        message: 'Product no actualizado'
                    });
                });
            }
        },

        components: {
            'notification' : Notification
        }
    }
</script>
