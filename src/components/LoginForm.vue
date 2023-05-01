<script setup>
  import { ref, onMounted } from "vue";
  let csrf_token = ref("");
  let FlashMessage = ref("");
  let danger = ref(false);
  let success = ref("");
  onMounted(() => {
    getCsrfToken();
  });
  function getCsrfToken() {
    fetch('/api/v1/csrf-token')
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
      })
    }
  function LoginUser() {
  let LoginForm =document.getElementById('LoginForm');
  let form_data = new FormData(LoginForm);
  fetch("/api/v1/auth/login", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
      }
    })
    .then(function (response) {
    return response.json();
    
    })
    .then(function (data) {
      if(data.errors){
        FlashMessage.value = data.errors;
        danger.value = true;
        clearFormData();
      }
      else{
        FlashMessage.value = "Login Successful!";
         success.value = true;
         danger.value = false;
         const userid = data.id
         localStorage.setItem('userid',userid)
         localStorage.setItem('username',form_data.get("username"));
         localStorage.setItem('JWT',data.token);
         clearFormData(); 
         window.location.href = '/';    
      }
    
    })
    .catch(function (error) {
      console.log(error);
    });
    }
    function clearFormData(){
       var data = document.querySelectorAll('input');
       data.forEach(input => input.value='');
    }
  
</script>

<template>
  <div class="heading">
    <h1 >Login</h1>
    <div class = "formbox">
  
    <div v-if="success" class = "alert alert-success" >{{FlashMessage}}</div>
    <div v-if ="danger" class = "alert alert-danger"> 
      <li v-for= "d in FlashMessage">{{d}}</li>
    </div>
    
    <form id = "LoginForm" @submit.prevent="LoginUser">

    <div class="form-group mb-3">
      <label for="username" class="form-label">Username</label>
      <br>
      <input type="text" name="username" class="formcontrol" />
    </div>

   
    <div class="form-group mb-3">
      <label for="password" class="form-label">Password</label>
      <br>
      <input type="text" name="password" class="formcontrol" />
    </div>

     
    <div class="form-group mb-3">
      <button type="submit"  class="btn btn-primary mb-3" >Login</button>
    </div>

    </form>
  </div>
  </div>
  
</template>



<style>

.heading{
 margin:auto; 
 justify-content: center;
 text-align:center;
}

.formbox{
  margin:auto;
  border: 2px solid gray;
  background-color:white;
  width:400px;
  box-shadow:0 0 6px;
  padding: 20px;
  justify-content: center;
}
label{
    font-weight: bold;
}

.form-group mb-3{
    padding: 10px;
}
</style>