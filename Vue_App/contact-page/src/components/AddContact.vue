<template>
    <form @submit="onSubmit" class="add-form form-control">
        <div>
            <label>Name: </label>
            <input type="text" v-model="name" name="name" placeholder="Name"/>
        </div>
        <div>
            <label>Phone Number: </label>
            <input type="text" v-model="phone_number" name="phone_number" placeholder="Phone Number"/>
        </div>
         <div>
            <label>Email: </label>
            <input type="text" v-model="email" name="email" placeholder="Email"/>
        </div>
        
        <input type="submit" value="Save Contact" class="btn btn-block"/>
    </form>
</template>

<script>
export default {
    name: 'AddContact',
    data() {
        return {
            name: '',
            phone_number: '',
            email: ''
        }
    },
    methods:{
        onSubmit(e){
            e.preventDefault()

            if(!this.name){
                alert('Please add a Name')
                return
            }

            if(!this.phone_number){
                alert('Please add a Phone Number')
                return
            }

            if(!this.email){
                alert('Please add a Email')
                return
            }


            const newContact = {
                name: this.name,
                phone_number: this.phone_number,
                email: this.email
            }

            this.$emit('add-contact', newContact)

            this.name = ''
            this.phone_number = ''
            this.email = ''
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