<script setup>
  import { ref, onMounted } from "vue";
  let FlashMessage = ref("");
  let danger = ref(false);
  let success = ref("");
  let csrf_token = ref("");
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

  function addPost() {
  let PostForm =document.getElementById('PostForm');
  let form_data = new FormData(PostForm);
  // Call API to add post
  fetch("/api/v1/users/<user_id>/posts", {
      method: "POST",
      body:form_data,
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
        FlashMessage.value = "Added Post Successfully!";
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
    <h1 >Add Post</h1>
    <div class = "formbox">
    <div v-if="success" class = "alert alert-success">{{FlashMessage}}</div>
    <div v-if ="danger" class = "alert alert-danger"> 
      <li v-for= "d in FlashMessage">{{d}}</li>
    </div>
    <form id="PostForm" @submit.prevent="addPost">
      <div>
        <label for="photo">Photo: </label>
        <input type="file" name="photo" required>
      </div>
      <div>
        <label for="caption">Caption: </label>
        <textarea name="caption" required></textarea>
      </div>
      <div>
        <a><button type="submit" class="btn btn-primary">Add Post</button></a>
      </div>
    </form>
  </div>
</div>
</template>


  
