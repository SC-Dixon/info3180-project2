<script setup>
import { RouterLink } from "vue-router";
import { ref, onMounted } from "vue";
  let posts = ref("");
  let csrf_token = ref("");
  onMounted(() => {
    getCsrfToken();
    fetchPosts();
  });

  function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    })
  }

function fetchPosts(){
  fetch("/api/v1/posts", {
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

function addLike(post_id){
  fetch("/api/v1/posts/<post_id>/like", {
    method: "POST",
    headers: {
    'X-CSRFToken': csrf_token.value
    }
  })
  .then(function(response){
    return response.json();
  })
  .then(function(data){
    return data
  })
  .catch(function(error){
    console.log(error);
  })
}
</script>

<template>
  <div>
    <h1>Explore Page</h1>
    <button type="submit" class=""><RouterLink to="/posts/new">New  Post</RouterLink></button>
      <div class="explorebox" v-for="(post,postindex) in posts" :key="postindex">
        <div class="postClass" v-for="(image,imageindex) in post" :key="imageindex">
          <RouterLink to="/users/<user_id>/posts">USER ID: {{ image.user_id }}</RouterLink>
          <img :src="'uploads/'+image.photo" alt="Post Photo"/>
          <p>Caption: {{ image.caption }}</p>
          <p>{{ image.created_on }}</p>
          <a><button @click="addLike(image.id)" class="btn btn-primary">Like</button></a>
        </div>
      </div>
 
  </div> 
</template>



<style>
.explorebox{
  margin:auto;
  padding: 20px;
}

.postClass{
  margin:auto;
  border: 2px solid gray;
  background-color:white;
  width:540px;
  box-shadow:0 0 6px;
  padding: 20px;

}

img{
  height:300px;
}
</style>