<template>
    <form @submit="onSubmit" class="add-form form-control">
        <div>
            <label>Name: </label>
            <input type="text" v-model="name" name="name">
        </div>
        <div>
            <label>Phone Number: </label>
            <input type="text" v-model="phone_number" name="phone_number" placeholder="Phone Number"/>
        </div>
         <div>
            <label>Email: </label>
            <input type="text" v-model="email" name="email" placeholder="Email"/>
        </div>
        
        <input type="submit" value="Update Contact" class="btn btn-block"/>
    </form>
</template>

<script>
export default {
    name: 'UpdateContact',
    props: {
        contact: Object
    },
    data() {
        return {
            name: this.contact.name,
            phone_number: this.contact.phone_number,
            email: this.contact.email
        }
    },
    methods:{
        async onSubmit(e){
            e.preventDefault()

            if(!this.name){
                alert('Name cannot be empty')
                return
            }

            let isnum = /^\d+$/.test(this.phone_number);
            if(!this.phone_number || this.phone_number.length == 11 || !isnum){
                alert('Please add a valid Phone Number')
                return
            }

            if(!this.email || !this.email.includes('@')){
                alert('Please add a valid Email')
                return
            }

            const updatedContact = {
                name: this.name,
                phone_number: this.phone_number,
                email: this.email
            }

            const result = await fetch(`/contact/${this.contact.id}`, {
                method: 'PUT',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(updatedContact)
            })

            const data = await result.json()
            const code = await result

            console.log(data)

            if(code.status !== 200){
                alert('Error updating contact')
                return
            }

            this.$emit('update-contact', data)
        }
    }
    
}
</script>

<style scoped>
.add-form{
    margin-bottom: 40px;
}

.form-control {
    margin: 20px 0;
}

.form-control label{
    display: block;
}

.form-control input{
    width: 100%;
    height: 40px;
    margin: 5px;
    padding: 3px 7px;
    font-size: 17px;
}

.form-control-check{
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.form-control-check label{
    flex: 1;
}

.form-control-check input{
    flex: 2;
    height: 20px;
}

.btn.btn-block{
    background: #32A0FF;
}
</style>