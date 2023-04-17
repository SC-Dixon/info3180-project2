<script setup>
import { ref } from "vue";
import { RouterLink } from "vue-router";

let message = ref("Hello World! This is a VueJS and Flask Starter Template.")

</script>


<template >
    
    <div class="container">
      <div class="text-center">
        <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
      </div>

    

      <div class= "box1">
      <i class='fas fa-camera'></i>
       <h1>Photogram</h1>
       <h2>Share photos of your favourite moments with friends, family and the world</h2>
      <button class ="b1"><RouterLink type="button" class="nav-link" to="/register">Register</RouterLink></button>
      <button class ="b2"><RouterLink type="button" class="nav-link" to="/login">Login</RouterLink></button>
      </div>
    </div>
</template>

<style>
.container{
  display:flex;
  padding: 10px;
}
 
.box1{
  border: 2px solid gray;
  box-shasow:0 0 6px;
  border-radius:10px;
  padding: 20px;
  justify-content: center;
}
.b1{
  background-color:green;
}

.b2{
  background-color:blue
}
</style>