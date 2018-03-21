<template>
    <div id="create-product">
        <h1>Crear Producto</h1>

        <p><router-link :to="{ name: 'all_products' }">Volver al menú</router-link></p>

        <notification v-bind:notifications="notifications"></notification>

        <form v-on:submit.prevent="addProduct">
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
                <button class="btn btn-primary">Create</button>
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

        methods: {
            addProduct: function()
            {
                // Validation
                var price = parseFloat(this.product.precio);
                if(isNaN(price))
                {
                    this.notifications.push({
                        type: 'danger',
                        message: 'El precio debe ser un numero'
                    });
                    return false;
                } else {
                    this.product.precio = this.product.precio;
                }

                this.$http.post('http://localhost:8098/api/products', this.product, {
                    headers : {
                        'Content-Type' : 'application/json'
                    }
                }).then((response) => {
                    this.notifications.push({
                        type: 'success',
                        message: 'Producto creado satisfactoriamente'
                    });
                }, (response) => {
                    this.notifications.push({
                        type: 'error',
                        message: 'Product no fue creado'
                    });
                });
            }
        },

        components: {
            'notification' : Notification
        }
    }
</script>
