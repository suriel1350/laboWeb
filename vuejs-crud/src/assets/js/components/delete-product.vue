<template>
    <div id="delete-product">
        <h1>Eliminar Producto {{ product.nombre }}</h1>

        <p><router-link :to="{ name: 'all_products' }">Volver al menú</router-link></p>

        <notification v-bind:notifications="notifications"></notification>

        <form v-on:submit.prevent="deleteProduct">
            <p><button class="btn btn-danger">Borrar Producto</button></p>
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

            deleteProduct: function()
            {
                this.$http.delete('http://localhost:8098/api/products/' + this.$route.params.product_id, this.product, {
                    headers : {
                        'Content-Type' : 'application/json'
                    }
                }).then((response) => {
                    this.$router.push({name: 'all_products'})
                }, (response) => {
                    this.notifications.push({
                        type: 'danger',
                        message: 'Producto no se pudo eliminar'
                    });
                });
            }
        },

        components: {
            'notification' : Notification
        }
    }
</script>
