<template>
    <header>
        <h1>{{title}}</h1>
        <Button @toggle-add-contact="$emit('toggle-add-contact')" :text="showAddContact ? 'Close' : 'Add Contact'" 
        :color="showAddContact ? 'red' : 'green'" />
    </header>
</template>

<script>
import Button from './Button'
    export default{
        name: 'Header',
        props: {
            title: String,
            showAddContact: Boolean
        },
        components:{
            Button
        }
    }
</script>

<style scoped>
    header{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
</style>