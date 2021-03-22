<template>
    <div class='contact'>
        <h3>
            {{contact.name}}
            <button class="btn" @dblclick="$emit('delete-contact', contact.id)">
                <i class="fas fa-times"></i>
            </button>        
        </h3>
        <p>{{contact.email}}</p>
        <p>{{contact.phone_number}}</p>
    </div>
</template>

<script>
export default {
    name: 'Contact',
    props: {
        contact: Object
    }
}
</script>

<style scoped>
.contact {
    background: #f4f4f4;
    margin: 15px;
    padding: 20px;
    cursor: pointer;
}

.contact h3{
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.contact button{
    background-color: #fff;
}

.fas {
    color: red;
}
</style>