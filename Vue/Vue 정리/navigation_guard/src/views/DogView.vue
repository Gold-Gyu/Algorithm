<template>
  <div>
    <h1>Dog View입니다.</h1>
    <p v-if="!imgSrc">{{ message }}</p>
    <img v-if="imgSrc" :src="imgSrc" alt="">
    <br>

  </div>
</template>

<script>
import axios from "axios"
export default {
    name : 'DogView',
    data() {
        return {
            imgSrc: null,
            message: "로딩중 ............"
        }
    },
    methods: {
        // axsios요청하기
        getDogImage() {
            const breed = this.$route.params.breed
            const dogImageSearchURL = `https://dog.ceo/api/breed/${breed}/images/random`
            
            axios({
                methods: 'get',
                url : dogImageSearchURL
            })
            .then((response) => {
                console.log(response)
                const dogImgSrc = response.data.message
                this.imgSrc = dogImgSrc
            })
            .catch((error) => {
                console.log(error)
                this.message = `${this.$route.params.bread}는 없는 품종입니다.`
                this.$router.push('/404')
            })
        }
    },
    created() {
        //접속을 하자마자
        this.getDogImage()
    }
}
</script>

<style>

</style>