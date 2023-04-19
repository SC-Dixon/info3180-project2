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

  function RegisterUser() {
  let RegisterForm =document.getElementById('RegisterForm');
  let form_data = new FormData(RegisterForm);

  fetch("/api/v1/register", {
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
        FlashMessage.value = "Registered Successfully!";
         success.value = true;
         danger.value = false;
         clearFormData();
         console.log(data);
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
    <h1 >Register</h1>
    <div class = "formbox">
    <div v-if="success" class = "alert alert-success">{{FlashMessage}}</div>
    <div v-if ="danger" class = "alert alert-danger"> 
      <li v-for= "d in FlashMessage">{{d}}</li>
    </div>
    
    <form id = "RegisterForm" @submit.prevent="RegisterUser">

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
      <label for="firstname" class="form-label">Firstname</label>
      <br>
      <input type="text" name="firstname" class="formcontrol" />
    </div>

     <div class="form-group mb-3">
      <label for="lastname" class="form-label">Lastname</label>
      <br>
      <input type="text" name="lastname" class="formcontrol" />
    </div>

     <div class="form-group mb-3">
      <label for="email" class="form-label">Email</label>
      <br>
      <input type="text" name="email" class="formcontrol" />
    </div>

     <div class="form-group mb-3">
      <label for="location" class="form-label">Location</label>
      <br>
      <input type="text" name="location" class="formcontrol" />
    </div>

     <div class="form-group mb-3">
      <label for="biography" class="form-label">Biography</label>
      <br>
      <input type="text" name="biography" class="formcontrol" />
    </div>

    <div class="form-group mb-3">
      <label for="profile_photo" class="form-label">Photo</label>
      <br>
      <input type="file" name="profile_photo" class="formcontrol" />
    </div>

    <div class="form-group mb-3">
      <a><button type="submit"  class="btn btn-primary mb-3" >Register</button></a>
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
  box-shasow:0 0 6px;
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