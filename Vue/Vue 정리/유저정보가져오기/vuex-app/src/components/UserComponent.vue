<template>
    <div>
        <h1>username: {{ user.username}}</h1>
        <h1>email: {{ user.email}}</h1>
    </div>
</template>

<script>
export default {
    name : "UserComponent",
    props : {
        user : Object
    }
}
</script>

<style>

</style>