<script setup>
import { ref } from "vue";
import { RouterLink } from "vue-router";
 
</script>


<template >

    
    <div class="container">
     
      <div class="text-center">
        <img alt="Home Page Picture" class="homepic" src="@/assets/homepic.jpg"  />
          
      </div>

      <div class= "box1">
      <div class ="top"><img alt="Home Page Picture" class="camera" src="@/assets/photo-camera.png" width="50" height="50"  /><h2>Photogram</h2>
      </div>
      
      
      <hr>
      <div class="buttons">
         <p>Share photos of your favourite moments with friends, family and the world</p>
         <br>
        <a href="/register"><button class="btn btn-primary mb-3 b1" >Register</button></a>
        <a href="/login"><button class="btn btn-primary mb-3 b2" >Login</button></a>
    
      </div>
     
       
      </div>
    </div>
</template>

<style scoped>
.homepic{
height:500px;
margin-right:10px;
}
.camera{
  float:left;
  
}
  
.top{padding-top:60px;}

h2{
  font-family: "Brush Script MT", cursive;
  font-weight: bold;
  font-size: 50px;
  
  
}
p{
  font-size: 20px;
}
 
.container{
  margin:auto;
  display:flex;
  flex-direction:row;
  padding: 20px;
}

 
.box1{
  border: 2px solid gray;
  background-color:white;
  width:300px;
  box-shasow:0 0 6px;
  padding: 20px;
  justify-content: center;
  text-align:center;
}
.b1{
  background-color:green;
  border-color:green;
  
  
}

.b2{
  margin-left:10px;
}
</style>