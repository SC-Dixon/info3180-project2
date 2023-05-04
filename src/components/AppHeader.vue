<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">Photogram</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link active">Home</RouterLink>
            </li>
            <li class="nav-item" id="explore1">
              <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
            </li>
            <li class="nav-item" id="profile1">
              <RouterLink class="nav-link" to="/users/<user_id>/posts">My Profile</RouterLink>
            </li>
            <li class="nav-item" id="post1">
              <RouterLink class="nav-link" to="/posts/new">Add Post</RouterLink>
            </li>
            <li class="nav-item" id="logout1">
              <RouterLink  class="nav-link"  to="/logout">Logout</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
   
        
</template>

<script>
import { RouterLink } from "vue-router";
window.onload = function(){

  let logoutEl =document.getElementById('logout1');
  let postEl =document.getElementById('post1');
  let profileEl =document.getElementById('profile1');
  let exploreEl =document.getElementById('explore1');
  let curuserid = sessionStorage.getItem("curuserid")
  console.log(curuserid)
  console.log(curuserid == null)
  if (curuserid == null){
    logoutEl.style.display = "none";
    postEl.style.display = "none";
    profileEl.style.display = "none";
    exploreEl.style.display = "none";
  }
}
</script>

<style>
/* Add any component specific styles here */
</style>