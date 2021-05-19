<template>
  <div class="login-container background">
    <div class="wrapper">
      <div class="debate-logo">
        <img src="../assets/motion-generator-logo.svg" alt="motion generator logo">
        <span>Easiest way to find a motion for debating</span>
      </div>
      <div class="registration-form-container">
        <form @submit="change">
          <h1>Enter new password</h1>
          <label for="password">Password</label>
          <input type="password" id="password" name="password">
          <button type="submit">Change password</button>
        </form>
        <hr class="line"/>
        <div class="login-text">
          <p><a href="/login">Back to log in.</a></p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        password: '',
        favorites: []
      }
    },
    props: ['uid', 'token'],
    methods : {
      change: async function(e){
        e.preventDefault()
        const response = await this.$store.dispatch('change', {
            password: password.value,
            token: this.$route.params.token, 
            uid: this.$route.params.uid
          })
        if (response) window.location.href = '/login'
      }
    }
  }
</script>
<style scoped>
</style>
