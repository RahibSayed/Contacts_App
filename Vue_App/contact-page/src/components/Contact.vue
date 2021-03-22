<template>
    <div class='contact'>
        <h3>{{contact.name}}</h3>
            <div class="btns">
                <button class="btn" @click="$emit('delete-contact', contact.id)">
                    <i class="fas fa-times"></i>
                </button> 
                    
                <button class="btn" @click="toggleUpdate">
                    <i class="fas fa-pencil-alt"></i>
                </button>
            </div>
        
        <p>{{contact.email}}</p>
        <p>{{contact.phone_number}}</p>

        <div v-show="toggle">
            <UpdateContact :contact="contact" @update-contact="updateContact"/>
        </div>
    </div>
</template>

<script>
import UpdateContact from './UpdateContact'

export default {
    name: 'Contact',
    props: {
        contact: Object
    },
    data() {
        return {
            toggle: false,
            contact: this.contact
        }
    },
    components: {
        UpdateContact
    },
    methods:{
        toggleUpdate(){
            this.toggle = !this.toggle
        },
        updateContact(updatedContact){
            console.log("Update",updatedContact)
            console.log("Contact",this.contact)
            this.contact = updatedContact
        }
    }
}
</script>

<style scoped>
.contact {
    background: #f4f4f4;
    margin: 40px;
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

.btns{
    float: right;
}
</style>