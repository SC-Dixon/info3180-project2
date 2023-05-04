<template>
 <div class="container">
  <h1>Explore Page</h1>
    
    
    <div class="twofields">
      <div class="card-container">
        <div v-for="post in posts" >
          <div class="card pt-2 rounded-top mt-4">
              <div class="card-header">
                <p class="card-text">{{post.caption}}</p>
              </div>
              <div class="card-body shadow-sm">
                <div class="card-img">
                      <img v-bind:src="post.photo" class="card-imgs2">
                  </div>
                  <p class="card-text">{{post.caption}}</p>
                  
              </div>
              <div class="card-footer">
                <div class="twofields">
                  <p>{{datefmt(post.created_on)}}</p>
                </div> 
                  
              </div>
          </div>
        </div>

      </div>
      <div>
        <button type="submit" class="btn btn-primary"><RouterLink to="/posts/new">New Post</RouterLink></button>
      </div>
    </div>
    
    
    
</div>
</template>



<script setup>
import { ref, onMounted } from "vue";
let posts = ref([]);
let users = ref([]);
let csrf_token = ref("");
let curuserid = sessionStorage.getItem("curuserid");
let userid = sessionStorage.getItem("userid");
console.log(userid == null)
console.log(curuserid == userid)
  if (userid == null){
    userid = curuserid;
    
  }
  if (curuserid == userid){
    userid = curuserid;
  }
  onMounted(() => {
    getCsrfToken();
    fetchPosts();
    fetchUser();
  });

  function datefmt(value) {
        const dateObj = new Date(value);
        return dateObj.toLocaleDateString('en-US', {
          day: 'numeric',
          month: 'short',
          year: 'numeric',
        });
      }

  function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    })
  }

  function fetchUser() {
        fetch(`/api/v1/users/${userid}`, {
          method: "GET",
          headers: {
            'X-CSRFToken': csrf_token.value
          }     
        })
        .then((response)=> response.json())
        .then((data) => {
          users.value = data.users;
          console.log(users);
        })
        .catch(function (error) {
          console.log(error);
        });
      }

function fetchPosts(){
  fetch('/api/v1/posts', {
      method: "GET",
      headers: {
      'X-CSRFToken': csrf_token.value
      }    
  })
    .then((response)=> response.json())
    .then((data) => {
      posts=data.posts;
      console.log(posts);
    })
    .catch(function (error) {
      console.log(error);
    });
}

function addLike(post_id){
  fetch('/api/v1/posts/<post_id>/like', {
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





<style>



.userpic{
  height: 20px;
  width: 20px;
  border-radius: 50%;
}

.card-imgs2{
  height:500px;
  width:450px;
}


</style>