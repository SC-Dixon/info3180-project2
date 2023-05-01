<script>
import { RouterLink } from "vue-router";

 
 export default {
  data(){
     return {
      csrf_token: '',
      FlashMessage:'',
      userid: localStorage.getItem('username'),
      };  
  },
  created() {
        this.getCsrfToken();
  },
  methods:{
  userlogout(){
    console.log("hello")
    let self = this;
    fetch("/api/v1/auth/logout", {
            method: 'POST',
            //body:{} ,
            headers: {
              'X-CSRFToken': this.csrf_token,
              'Authorization': 'Bearer' + localStorage.getItem('JWT')           
            }
        })
        .then((response) => response.json())
        .then((data) => { 
            self.FlashMessage =  data.message;
            console.log(data);
            localStorage.removeItem('username');
            localStorage.removeItem('JWT'); 
            window.location.href = '/';
            
              
      })
      .catch(function (error) {
      console.log(error);
      self.FlashMessage =  "Logout Unsucessful, are you sure you logged in?";
    });
},
getCsrfToken() {
            let self = this;
            fetch('/api/v1/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
      }
 }}
</script>

<template >

    
    <div class="container">
        <div class = "alert" >{{FlashMessage}}</div>
      <div class= "box1"> 
      <h2>Photogram</h2>
      <hr>
      <div class="buttons">
         <p>Are you sure you want to logout?</p>
        <a @click="userlogout()"><button class="btn btn-primary mb-3 b1" >YES</button></a>
        <a href="/"><button class="btn btn-primary mb-3 b2" >NO</button></a>
    
      </div>
     
       
      </div>
    </div>
</template>

<style scoped>

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

}

.container > div{
  width:500px;
  padding: 20px;
  text-align:center;
   
}
 
 
.box1{
  border: 2px solid gray;
  background-color:white;
  width:400px;
  box-shadow:0 0 6px;
  padding: 20px;
  justify-content: center;
}
.b1{
  background-color:green;
  border-color:green;
  
}

.b2{
  margin-left:10px;
  
}
</style>
