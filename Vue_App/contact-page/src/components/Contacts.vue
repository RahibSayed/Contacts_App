<template>
    <div>   
        <div :key="contact.id" v-for="contact in contacts">
            <Contact 
            @delete-contact="$emit('delete-contact', contact.id)" :contact="contact"
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
    emits: ['delete-contact']
}
</script>