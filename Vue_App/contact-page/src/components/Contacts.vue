<template>
    <div>   
        <div :key="contact.id" v-for="contact in contacts">
            <Contact 
            @delete-task="$emit('delete-task', contact.id)" :contact="contact"
            />
        </div>
    </div>
</template>

<script>
import Contact from './Contact'

export default {
    name: 'Contacts',
    props: {
        contacts: Array
    },
    components: {
        Contact
    },
    emits: ['delete-task']
}
</script>