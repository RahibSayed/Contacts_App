<template>
    <div class='contact'>
        <h3>
            {{contact.name}}
            <i @dblclick="$emit('delete-task', contact.id)" class="fas fa-times"></i>
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

.fas {
    color: red;
    cursor: grab;
    padding: 3px;
}
</style>