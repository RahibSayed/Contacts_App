<template>
    <div>
        <nav class="navbar navbar-light bg-light">
            <form class="form-inline">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"  v-model="search"/>
                <button class="btn btn-outline-success" @click="onClick">Search</button>
            </form>
        </nav>
    </div>
</template>

<script>
export default {
    name:'Search',
    data(){
        return {
            search: ''
        }
    },
    methods:{
        onClick(e){
            e.preventDefault()
            this.$emit('search-contact', this.search)
        }
    }
}
</script>