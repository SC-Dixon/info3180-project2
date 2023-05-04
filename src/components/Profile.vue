<template>
    <div class="container p-1">
      <div v-for="u in users" class="card-deck">
        <div class="card shadow w-100" Style="height: 100%">
            <div class="row no-gutters">
                <div class="col-md-2">
                    <img v-bind:src="u.photo" class="card-imgs rounded-start p-2">
                </div>
                <div class="col-md-10">
                    <div class="card-block px-2">
                      <div class="twofields">
                        <div class="tgroup">
                          <h4 class="card-title pt-2 pb-3">{{u.name}} </h4>
            
                        <p class="card-text text-muted pb-0"> {{ u.location }}<br>
                          Member Since {{ datefmt(u.joined_on)}}</p>
                        <p class="card-text text-muted"> {{ u.biography }}</p>
                        </div>
                        <div class="tgroup2">
                          <div class="metricsContainer pt-3 pr-4">
                            <div class="twofields">
                              <div class="metric">
                                  <p1>{{ u.numposts }}</p1>
                                  <p2 class="text-muted">Posts</p2>
                              </div>
                              <div class="metric">
                                  <p1>{{ u.numfollowers }}</p1>
                                  <p2 class="text-muted">Followers</p2>
                              </div>
                          </div>
                          </div>
                          <div id="followMetric">
                            <div v-if="u.isFollowed"  class="btnContainer pt-5">
                              <button class="btn btn-success" id="followingBtn">Following</button>
                            </div>
                            <div v-else-if="userid == curuserid" class="btnContainer pt-5">
                              <button ref="myButton" @click="handleClick(u.id)" class="btn btn-primary hide" id="followButton">Follow</button>
                            </div>
                            <div v-else class="btnContainer pt-5">
                              <button ref="myButton" @click="handleClick(u.id)" class="btn btn-primary hide" id="followButton">Follow</button>
                            </div>
                          </div>
                        </div>
                          
                        
                      </div> 
                        
    
                    </div>
                </div>
            </div>
            
        </div>
      </div>
     
        <h2>Posts</h2>
        <div class="" id="image-grid">  
          <div v-for="post in posts" >  
              <img v-bind:src="post.photo" class="card-imgs rounded-start">
                        
          </div>
        </div>

    </div>
    <!-- <div class="explorebox" v-for="(post,postindex) in posts" :key="postindex">
        <div class="postClass" v-for="(image,imageindex) in post" :key="imageindex">
          <p>USER ID: {{ image.user_id }}</p>
          <img :src="'uploads/'+image.photo" alt="Post Photo"/>
          <p>Caption: {{ image.caption }}</p>
          <p>{{ image.created_on }}</p>
      <ul>
        <li v-for="post in posts" :key="post.id">
          <img :src="'../uploads/' + post.photo" alt="Post photo" />
          <p>{{ post.caption }}</p>
        </li>
      </ul> 
        </div>
    </div>-->
  </template>
  
  <script setup>
  import { ref, onMounted, nextTick } from "vue";
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
    fetchUserPosts();
    fetchUser();
  });

  
      async function handleClick(uid) {
        await nextTick(); // Wait for the component to be mounted
        const myButton = document.getElementById("followButton");
        myButton.classList.remove('btn-primary');
        myButton.classList.add('btn-success');
        myButton.textContent = 'Following';
        fetch(`/api/users/${uid}/follow`, {
          method: "GET",
          headers: {
            'X-CSRFToken': csrf_token.value
          }     
        })
        .then((response)=> response.json())
        .then((data) => {
          console.log(data.message);
        })
        .catch(function (error) {
          console.log(error);
        });

      }
      
      function datefmt(value) {
        const dateObj = new Date(value);
        return dateObj.toLocaleDateString('en-US', {
          month: 'long',
          year: 'numeric',
        });
      }
    
      function getCsrfToken() {
        fetch('/api/v1/csrf-token')
          .then((response) => response.json())
          .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
          });
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
      
      function fetchUserPosts() {
        fetch(`/api/v1/users/${userid}/posts`, {
          method: "GET",
          headers: {
            'X-CSRFToken': csrf_token.value
          }     
        })
        .then((response)=> response.json())
        .then((data) => {
          posts.value = data.posts;
          console.log(posts);
        })
        .catch(function (error) {
          console.log(error);
        });
      }
    
  </script>

<style>
.card-imgs{
    height:200px;
    width: 170px;
}

#image-grid{
    display: flex;
    flex-wrap: wrap;
}

#image-grid img{
    width:390px;
    height:300px;
    margin:10px;
}

.twofields{
    display: flex;
    justify-content: space-between;
}

.metricsContainer .metricsCount{
    text-align: center;

}

.metric{
    display: inline-block;
    padding: 10px 10px;
    vertical-align: middle;
}

.metric p2{
    position: relative;
    top: 30px;
    right: 30px;
    font-weight: bold;
}

.metric p1{
    font-weight: bolder;

}



.hide {
  display: none;
}


</style>