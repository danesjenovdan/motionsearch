<template>
  <div class="login-container background">
    <div class="wrapper">
      <div class="debate-logo">
        <img src="../assets/motion-generator-logo.svg" alt="motion generator logo">
        <span>Easiest way to find a motion for debating</span>
      </div>
      <div class="registration-form-container">
        <form @submit="register">
          <h1>Register your account</h1>
          <label for="username">Username</label>
          <input type="text" id="username" name="username">
          <label for="email">Email address</label>
          <input type="email" id="email" name="email">
          <label for="password">Password</label>
          <input type="password" id="password" name="password">
          <label for="confirmpwd">Confirm password</label>
          <input type="password" id="confirmpwd" name="confirmpwd">
          <button type="submit" @click="register">Submit</button>
        </form>
        <hr class="line"/>
        <div class="login-text">
          <p>Already have an account? <a href="/login">Log in.</a></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        confirmpwd: '',
        email: '',
        favorites: []
      }
    },
    methods : {
      validate(password, confirmpwd) {
        return password === confirmpwd
      },
      register: async function(e){
        e.preventDefault()
        if (!password.value || !this.validate(password.value, confirmpwd.value)) return false
        const response = await fetch('https://motion-search-backend.lb.djnd.si/api/v1/users/', {
          method: 'POST', // *GET, POST, PUT, DELETE, etc.
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: username.value,
            password: password.value,
            email: email.value,
            favorites: []
          }) // body data type must match "Content-Type" header
        });
        return response.json();
      }
    }
  }
</script>

<style scoped lang="scss">
</style>
