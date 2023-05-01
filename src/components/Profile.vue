<template>
    {{ posts }}
    <div class="explorebox" v-for="(post,postindex) in posts" :key="postindex">
        <div class="postClass" v-for="(image,imageindex) in post" :key="imageindex">
          <p>USER ID: {{ image.user_id }}</p>
          <img :src="'uploads/'+image.photo" alt="Post Photo"/>
          <p>Caption: {{ image.caption }}</p>
          <p>{{ image.created_on }}</p>
      <!-- <ul>
        <li v-for="post in posts" :key="post.id">
          <img :src="'../uploads/' + post.photo" alt="Post photo" />
          <p>{{ post.caption }}</p>
        </li>
      </ul> -->
        </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  let posts = ref("");
  let csrf_token = ref("");
  onMounted(() => {
    getCsrfToken();
    fetchUser();
  });

  function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    })
  }

function fetchUser(){
  fetch("/api/v1/users/<user_id>/posts", {
      method: "GET",
      headers: {
      'X-CSRFToken': csrf_token.value
      }     
  })
    .then((response)=> response.json())
    .then((data) => {
      posts=data
      console.log(posts)
    })
    .catch(function (error) {
      console.log(error);
    });
}

  </script>

<style>

</style>